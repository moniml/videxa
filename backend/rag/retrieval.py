import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./db")

# Try to get collection, if it doesn't exist, create an empty one
try:
    collection = client.get_collection("video_chunks")
except Exception as e:
    print(f"Collection not found, creating new one: {e}")
    collection = client.create_collection("video_chunks")

model = SentenceTransformer(
    "BAAI/bge-small-en-v1.5"
)

def retrieve(query):
    try:
        query_embedding = model.encode([query])

        results = collection.query(
            query_embeddings=query_embedding.tolist(),
            n_results=3
        )

        if results and results.get("documents"):
            return results["documents"][0]
        else:
            return ["No relevant content found in the video."]
    except Exception as e:
        print(f"Retrieval error: {e}")
        return ["Error retrieving content from video."]