"""Task 3: compare three chunking methods and TF-IDF / real sentence embeddings."""
import csv,json,time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from task2_chunks import make_chunks
from sentence_transformers import SentenceTransformer

def evaluate(scores,chunks,items):
    hits,reciprocal=[],[]
    for row,q in zip(scores,items):
        if q["doc"] is None: continue
        top=np.argsort(-row,kind="stable")[:3]
        good=[rank for rank,i in enumerate(top,1)
              if chunks[i]["doc"]==q["doc"] and q["evidence"] in chunks[i]["text"]]
        hits.append(bool(good)); reciprocal.append(1/good[0] if good else 0)
    return (float(np.mean(hits)),float(np.mean(reciprocal))) if hits else (None,None)

def main():
    docs=json.load(open("corpus.json",encoding="utf-8"))
    items=json.load(open("queries.json",encoding="utf-8"))
    assert len(docs)>=5 and len(items)>=10
    for q in items:
        assert q["split"] in {"dev","test"}
        if q["doc"] is not None: assert q["evidence"] in docs[q["doc"]]
    t=time.perf_counter()
    model=SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2",device="cpu")
    print("Model load seconds",round(time.perf_counter()-t,3))
    query_texts=[q["query"] for q in items]
    logs=[]
    for strategy in ["0","10","sentence"]:
        chunks=make_chunks(docs,strategy); texts=[c["text"] for c in chunks]
        lengths=[len(model.tokenizer(x,truncation=False)["input_ids"]) for x in texts+query_texts]
        if max(lengths)>model.max_seq_length: raise ValueError("Model token limit exceeded")
        for method in ["tfidf","embedding"]:
            t=time.perf_counter()
            if method=="tfidf":
                vec=TfidfVectorizer(); C=vec.fit_transform(texts); Q=vec.transform(query_texts)
            else:
                C=model.encode(texts,normalize_embeddings=True)
                Q=model.encode(query_texts,normalize_embeddings=True)
            encode_s=time.perf_counter()-t
            t=time.perf_counter()
            scores=(Q@C.T).toarray() if method=="tfidf" else Q@C.T
            search_s=time.perf_counter()-t
            for split in ["dev","test"]:
                ids=[i for i,q in enumerate(items) if q["split"]==split]
                print(strategy,method,split,"Hit@3/MRR@3",evaluate(scores[ids],chunks,[items[i] for i in ids]),
                      "chunks",len(chunks),"encode/search",round(encode_s,4),round(search_s,4))
            for row,q in zip(scores,items):
                for rank,i in enumerate(np.argsort(-row,kind="stable")[:3],1):
                    c=chunks[i]
                    logs.append(dict(strategy=strategy,method=method,query=q["query"],split=q["split"],
                      rank=rank,score=float(row[i]),chunk_id=c["id"],doc=c["doc"],
                      start=c["start"],end=c["end"],text=c["text"],answerable=q["doc"] is not None))
    with open("retrieval_log.csv","w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=list(logs[0])); w.writeheader(); w.writerows(logs)
    print("Saved retrieval_log.csv with",len(logs),"ranked rows.")
if __name__=="__main__": main()
