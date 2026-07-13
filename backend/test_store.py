from rag.embeddings import (
    chunk_text,
    create_embeddings
)
from rag.vectorstore import store_chunks

with open(
    "transcripts/WIN_20260527_20_56_55_Pro.txt",
    "r",
    encoding="utf-8"
) as f:
    transcript = f.read()

chunks = chunk_text(transcript)

embeddings = create_embeddings(chunks)

store_chunks(chunks, embeddings)