import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

print("DEBUG KEY LOADED:", "✓" if API_KEY else "✗ NOT SET")

# Create client with fallback if needed
if not API_KEY:
    print("⚠️ WARNING: OPENROUTER_API_KEY not set. Using demo mode.")
    client = None
else:
    client = OpenAI(
        api_key=API_KEY,
        base_url="https://openrouter.ai/api/v1"
    )

def generate_answer(query, context):
    try:
        # If no API key, return demo answer
        if not client:
            return f"Demo Answer: Based on the video content, here's what I found about '{query}'.\n\nNote: Please set OPENROUTER_API_KEY environment variable to enable AI-powered answers."
        
        context_text = " ".join(context) if isinstance(context, list) else context
        
        prompt = f"""Context from video:
{context_text}

Question:
{query}

Please provide a concise answer based on the video content."""

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content
    except Exception as e:
        print(f"Generator error: {e}")
        return f"Error generating answer: {str(e)}"