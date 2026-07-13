from rag.embeddings import (
    chunk_text,
    create_embeddings
)

with open(
    "transcripts/WIN_20260527_20_56_55_Pro.txt",
    "r",
    encoding="utf-8"
) as f:
    transcript = f.read()

chunks = chunk_text(transcript)

vectors = create_embeddings(chunks)

print("Chunks:", len(chunks))
print("Embeddings:", len(vectors))
print("Vector Size:", len(vectors[0]))