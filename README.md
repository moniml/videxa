# Videxa - AI Video Understanding Assistant

## Overview

Videxa is an AI-powered video question-answering system that allows users to upload videos, generate transcripts, and ask questions about the video content.

The application uses a Retrieval-Augmented Generation (RAG) pipeline to process video information. It converts video speech into text, creates embeddings, stores them in a vector database, retrieves relevant context, and generates answers using an LLM.

---

## Features

* Upload video files.
* Extract audio from videos.
* Generate transcripts using Whisper.
* Split transcripts into smaller chunks.
* Create text embeddings.
* Store embeddings for similarity search.
* Ask questions based on uploaded videos.
* Generate context-based answers using LLM.

---

## Architecture

```
Video Upload
      |
      v
Audio Extraction (FFmpeg)
      |
      v
Speech To Text (Whisper)
      |
      v
Transcript Processing
      |
      v
Text Chunking
      |
      v
Embedding Generation
      |
      v
Vector Database
      |
      v
Similarity Retrieval
      |
      v
LLM Response Generation
      |
      v
Answer
```

---

## Technology Stack

### Backend

* Python
* Flask
* Flask REST API
* Flask-CORS

### Frontend

* HTML
* CSS
* JavaScript
* Fetch API

### Artificial Intelligence

* Generative AI
* Large Language Models (LLM)
* Retrieval-Augmented Generation (RAG)
* Natural Language Processing (NLP)
* Semantic Search
* Text Embeddings

### Speech Processing

* OpenAI Whisper
* Automatic Speech Recognition (ASR)
* FFmpeg

### Vector Search

* Embedding Models
* Vector Database
* Similarity Search

### Development Tools

* Git
* GitHub
* Visual Studio Code
* Python Virtual Environment

---

## Project Workflow

1. User uploads a video through the frontend.

2. Backend receives the video and extracts audio using FFmpeg.

3. Whisper converts the audio into a text transcript.

4. The transcript is divided into smaller chunks.

5. Embedding models convert text chunks into vector representations.

6. Vectors are stored in a vector database.

7. User queries are matched with relevant transcript chunks.

8. The retrieved context is passed to the LLM to generate an answer.



---

### Backend Setup

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run backend:

```bash
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000
```

---

## Future Improvements

* Multilingual video support
* Quiz generation from videos
* Cloud deployment
* User authentication

---

## Developer

Monica M
AI and Machine Learning Student
