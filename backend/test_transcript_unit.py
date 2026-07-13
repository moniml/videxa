import sys
from pathlib import Path

import whisper


class FakeModel:
    def transcribe(self, audio_path):
        return {"text": ["Hello", "world"]}


def test_generate_transcript_writes_normalized_text(tmp_path, monkeypatch):
    monkeypatch.setattr(whisper, "load_model", lambda name: FakeModel())
    monkeypatch.chdir(tmp_path)
    sys.modules.pop("rag.transcript", None)

    from rag import transcript as transcript_module

    transcript = transcript_module.generate_transcript("sample.mp4")

    assert transcript == "Hello\nworld"
    assert (tmp_path / "transcripts" / "sample.txt").read_text(encoding="utf-8") == "Hello\nworld"


def test_generate_transcript_creates_output_dirs(tmp_path, monkeypatch):
    monkeypatch.setattr(whisper, "load_model", lambda name: FakeModel())
    monkeypatch.chdir(tmp_path)
    sys.modules.pop("rag.transcript", None)

    from rag import transcript as transcript_module

    def fake_run(args, **kwargs):
        return None

    monkeypatch.setattr(transcript_module.subprocess, "run", fake_run)

    transcript_module.generate_transcript("sample.mp4")

    assert (tmp_path / "audio").exists()
    assert (tmp_path / "transcripts").exists()
