from rag.transcript import generate_transcript

video = "uploads/WIN_20260527_20_56_55_Pro.mp4"

transcript = generate_transcript(video)

print(transcript)