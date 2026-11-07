import json
from task2_chunks import windows, sentence_chunks, make_chunks
from guided_chatbot import build_bot, reply

def main():
    assert windows("") == []
    assert windows("one two") == [(0,7)]
    try: windows("a b",2,2)
    except ValueError: pass
    else: raise AssertionError("Invalid overlap was accepted")
    text="A short sentence. Another short sentence."
    for a,b in sentence_chunks(text):
        assert text[a:b].strip()
    docs=json.load(open("corpus.json",encoding="utf-8"))
    assert len(docs)>=5
    chunks=make_chunks(docs,"sentence")
    for c in chunks:
        assert docs[c["doc"]][c["start"]:c["end"]]==c["text"]
    bot=build_bot("tfidf")
    assert "source:" in reply(bot,"How do I reset my password?")
    assert reply(bot,"")=="Please enter a question."
    assert "Possible matches" in reply(bot,"password recovery")
    assert "No matching FAQ" in reply(bot,"volcano geology")
    print("All Lab 6 local checks passed.")
if __name__=="__main__": main()
