"""Task 1: compare whitespace and Unicode word-like tokenization."""
import re
samples = [
    "AI, search!",
    "I can't log in.",
    "help@example.com",
    "CS4944 version 2.1",
    "",
    "یہ ایک مثال ہے",
]
for text in samples:
    whitespace = text.split()
    words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
    print("Original:", repr(text))
    print("Whitespace:", whitespace, "count =", len(whitespace))
    print("Word-like:", words, "count =", len(words))
    print("-" * 45)
assert re.findall(r"\b\w+\b", "", flags=re.UNICODE) == []
print("Tokenization checks passed.")
try:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
    for text in samples[:2]:
        print("Model subwords:", repr(text), model.tokenizer.tokenize(text))
except Exception as exc:
    print("Optional model-tokenizer comparison not run:", type(exc).__name__, str(exc)[:180])
