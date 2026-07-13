from rag.embeddings import chunk_text

with open(
    "transcripts/WIN_20260527_20_56_55_Pro.txt",
    "r",
    encoding="utf-8"
) as f:

    transcript = f.read()

chunks = chunk_text(transcript)

print("Total Chunks:", len(chunks))

for i, chunk in enumerate(chunks[:3]):
    print("\nChunk", i + 1)
    print(chunk)