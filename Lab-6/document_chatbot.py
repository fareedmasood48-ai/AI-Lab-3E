"""Task 3: interactive confirmation-based document evidence browser."""
import json
from task2_chunks import make_chunks
from lab6_search import Retriever
if __name__=="__main__":
    docs=json.load(open("corpus.json",encoding="utf-8"))
    try: engine=Retriever(make_chunks(docs,"sentence"),"embedding")
    except Exception as exc:
        print("Embedding backend unavailable:",type(exc).__name__,exc)
        print("Install requirements and ensure the model can be downloaded.")
        raise SystemExit(1)
    print("Evidence assistant. Type exit to stop.")
    while True:
        try: query=input("Question: ")
        except (EOFError,KeyboardInterrupt): break
        if query.strip().lower()=="exit": break
        hits=engine.search(query)
        if not hits:
            print("No candidate evidence; rephrase or contact a human."); continue
        print("Candidate evidence; relevance must be checked:")
        for n,(r,s) in enumerate(hits,1):
            print(n,r["id"],f"{s:.3f}","characters",r["start"],r["end"])
        choice=input("Choose 1-3 to inspect; Enter if none apply: ")
        if not choice.isdigit() or not 1<=int(choice)<=len(hits):
            print("No answer selected. Rephrase or contact a human."); continue
        r,s=hits[int(choice)-1]
        print("Retrieved passage:",r["text"])
        print("Source:",r["doc"],"characters",r["start"],r["end"])
