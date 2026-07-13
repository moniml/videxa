from rag.transcript import extract_audio

video = "uploads/WIN_20260527_20_56_55_Pro.mp4"

audio = extract_audio(video)

print("Audio Saved:", audio)