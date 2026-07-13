import os
import subprocess

import whisper

model = None


def get_model_name():
    return os.getenv("WHISPER_MODEL", "tiny")


def get_model():
    global model
    if model is None:
        try:
            model = whisper.load_model(get_model_name())
        except Exception:
            model = whisper.load_model("tiny")
    return model


def _normalize_transcript(transcript):
    if isinstance(transcript, list):
        return "\n".join(str(item) for item in transcript)
    return str(transcript)


def extract_audio(video_path):

    filename = os.path.splitext(
        os.path.basename(video_path)
    )[0]

    audio_path = f"audio/{filename}.wav"

    os.makedirs(os.path.dirname(audio_path), exist_ok=True)

    subprocess.run([
        "ffmpeg",
        "-i",
        video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        audio_path,
        "-y"
    ])

    return audio_path


def generate_transcript(video_path):

    audio_path = extract_audio(video_path)

    result = get_model().transcribe(audio_path)

    transcript = _normalize_transcript(result["text"])

    filename = os.path.splitext(
        os.path.basename(video_path)
    )[0]

    transcript_file = f"transcripts/{filename}.txt"

    os.makedirs(os.path.dirname(transcript_file), exist_ok=True)

    with open(transcript_file, "w", encoding="utf-8") as f:
        f.write(transcript)

    return transcript