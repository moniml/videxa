import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from rag.retrieval import retrieve
from rag.generator import generate_answer
from rag.transcript import generate_transcript
from rag.embeddings import chunk_text, create_embeddings
from rag.vectorstore import store_chunks

# ================= APP =================
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# ================= CONFIG =================
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ================= STATE =================
latest_video_path = None
video_processed = False


# ================= HOME =================
@app.route("/")
def home():
    return "Videxa API Running"


# ================= UPLOAD VIDEO =================
@app.route("/upload", methods=["POST"])
def upload_video():
    global latest_video_path, video_processed

    if "video" not in request.files:
        return jsonify({"error": "No video file received"}), 400

    file = request.files["video"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(file_path)
    latest_video_path = file_path
    video_processed = False

    try:
        # ✅ Generate transcript from video
        print(f"📝 Generating transcript from {file_path}...")
        transcript = generate_transcript(file_path)
        
        # ✅ Chunk the transcript
        print("✂️ Chunking transcript...")
        chunks = chunk_text(transcript)
        
        # ✅ Create embeddings
        print("🧠 Creating embeddings...")
        embeddings = create_embeddings(chunks)
        
        # ✅ Store in vector database
        print("💾 Storing in database...")
        store_chunks(chunks, embeddings)
        
        video_processed = True
        
        return jsonify({
            "message": "Video processed successfully",
            "video_path": file_path,
            "chunks_count": len(chunks)
        })
    except Exception as e:
        print(f"❌ Error processing video: {e}")
        video_processed = False
        return jsonify({
            "error": f"Failed to process video: {str(e)}",
            "message": "Video uploaded but processing failed. Check backend logs."
        }), 500


# ================= ASK QUESTION =================
@app.route("/ask", methods=["POST"])
def ask():
    global latest_video_path, video_processed

    data = request.get_json()

    if not data or "query" not in data:
        return jsonify({"error": "Missing query"}), 400

    query = data["query"]

    if not latest_video_path or not video_processed:
        return jsonify({"error": "No video processed yet. Please upload a video first."}), 400

    try:
        # ================= RAG FLOW =================
        context = retrieve(query)
        answer = generate_answer(query, context)

        return jsonify({
            "answer": answer
        })
    except Exception as e:
        print(f"❌ Error generating answer: {e}")
        return jsonify({
            "error": f"Failed to generate answer: {str(e)}"
        }), 500


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=False, use_reloader=False)