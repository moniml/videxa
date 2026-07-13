from rag.retrieval import retrieve
from rag.generator import generate_answer
import os
from dotenv import load_dotenv

load_dotenv()

query = "What are the candidate's technical skills?"
chunks = retrieve(query)

context = "\n".join(chunks)

answer = generate_answer(query, context)

print("\n=== ANSWER ===")
print(answer)