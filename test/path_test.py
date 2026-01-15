from pathlib import Path
import simpleaudio as sa
import threading

BASE_DIR = Path(__file__).resolve().parents[1]
HOME_DIR = BASE_DIR / "src" / "assets" / "sounds" / "london.wav"

def _play():
    obj = sa.WaveObject.from_wave_file(str(HOME_DIR))
    obj.play()

threading.Thread(target=_play,daemon=True).start()

while True:
    print('Loop')