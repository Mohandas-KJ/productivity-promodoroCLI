from pathlib import Path
import simpleaudio as sa
import threading, subprocess

BASE_DIR = Path(__file__).resolve().parents[1]
HOME_DIR = BASE_DIR / "src" / "assets" / "sounds" / "london.wav"

print(HOME_DIR)

try:
    subprocess.Popen([
            "powershell.exe",
            "-NoProfile",
            "-Command",
            f"(New-Object Media.SoundPlayer '{str(HOME_DIR)}').PlaySync()"
        ])
except Exception:
    print(Exception)