from rag.retrieval import retrieve

query = "What is this video about?"

results = retrieve(query)

print("\nRetrieved Chunks:\n")

for i, chunk in enumerate(results):
    print(f"\nChunk {i+1}")
    print(chunk)