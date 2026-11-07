# Lab 6 — NLP Fundamentals
Python 3.10+ recommended. Create/activate a virtual environment, then run:
`python -m pip install -r requirements.txt`

Task 1:
- `python task1_tokens.py`
- `python guided_chatbot.py` (try exact FAQ, paraphrase, empty input and `exit`)

Task 2:
- `python task2_chunks.py`
- `python task2_semantic_check.py`
- `python -c "from task2_chunks import make_chunks; import json; d=json.load(open('corpus.json')); print(len(make_chunks(d,'0')),len(make_chunks(d,'10')),len(make_chunks(d,'sentence')))"`

Task 3:
- `python task3_retrieval.py` (downloads the pretrained encoder on first run; CPU is supported)
- `python document_chatbot.py`

The corpus and policies are synthetic teaching data, not real university policies.
Embedding runs require internet access for the first model download. TF-IDF tasks run locally.

## Additional validation
Run `python lab6_checks.py` to check source offsets, chunking and FAQ fallback behavior.
