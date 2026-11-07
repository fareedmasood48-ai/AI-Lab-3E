"""Task 1: source-attributed FAQ chatbot with conservative confirmation."""
from lab6_search import Retriever
FAQ = [
 {"id":"faq:password","question":"How do I reset my password?",
  "answer":"Use the recovery link on the login page.","source":"it_help.txt"},
 {"id":"faq:submit","question":"Where do I submit my assignment?",
  "answer":"Use the assignment upload page in the learning portal.","source":"assessment.txt"},
 {"id":"faq:late","question":"Can illness justify a late submission?",
  "answer":"Request an extension with medical evidence before the deadline.","source":"handbook.txt"},
 {"id":"faq:account","question":"How can I recover my account?",
  "answer":"Use the account recovery link and follow the verification steps.","source":"account_guide.txt"},
 {"id":"faq:contact","question":"How do I contact IT support?",
  "answer":"Send a support request through the IT help desk portal.","source":"it_help.txt"},
]
def build_bot(backend="tfidf"):
    records = [dict(r, text=r["question"]+" "+r["answer"]) for r in FAQ]
    return Retriever(records, backend)
def reply(engine, query):
    if not query.strip():
        return "Please enter a question."
    for r in FAQ:
        if query.strip().casefold() == r["question"].casefold():
            return r["answer"] + " [source: " + r["source"] + "]"
    hits = engine.search(query)
    if not hits:
        return "No matching FAQ. Please contact the help desk."
    return "Possible matches; choose or rephrase your question:\n" + "\n".join(
        r["question"] + f" (similarity {score:.3f})" for r,score in hits)
if __name__ == "__main__":
    engine = build_bot()
    print("FAQ assistant. Type exit to stop.")
    while True:
        try: query = input("You: ")
        except (EOFError, KeyboardInterrupt): break
        if query.strip().lower() == "exit": break
        print("Bot:", reply(engine, query))
