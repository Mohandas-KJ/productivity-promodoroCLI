# This File maintains the CODE
# for user alerts

# Imports
from productivity.commons import platrad as pt
import os 
import simpleaudio as sa
from pathlib import Path

def beep(frequency, tp_ms):

    #Check if Windows and Play the sound
    try:
        if pt.isWindows():
            import winsound
            winsound.Beep(frequency,tp_ms)
            return
    except Exception:
        pass

    #Fallback, if none is possible
    print("\a",end="",flush=True)

def vibrate(vibration):
    #Additional Vibration feature if it's on Andoid's Termux
    try:
        if pt.isTermux():
            os.system(f"termux-vibrate -d {vibration}")
            return
    except Exception:
        pass

def playAudio(tid):

    GEN_DIR = Path(__file__).resolve().parent
    TONE_DIR = GEN_DIR / "assets" / "sounds"

    match tid:
        case 1:
            wav_obj = sa.WaveObject.from_wave_file(TONE_DIR / "digital_clock.wav")
            wav_obj.play()
        case 2:
            wav_obj = sa.WaveObject.from_wave_file(TONE_DIR / "doodle.wav")
            wav_obj.play()
        case 3:
            wav_obj = sa.WaveObject.from_wave_file(TONE_DIR / "london.wav")
            wav_obj.play()
        case 4:
            wav_obj = sa.WaveObject.from_wave_file(TONE_DIR / "techtonic.wav")
            wav_obj.play()
        case 5:
            wav_obj = sa.WaveObject.from_wave_file(TONE_DIR / "tick-tock.wav")
            wav_obj.play()
        case 6:
            wav_obj = sa.WaveObject.from_wave_file(TONE_DIR / "trap.wav")
            wav_obj.play()


def Alert(is_silent, tone, seq):
    if is_silent and pt.isWindows():
        if seq:
            beep(1500,700)
        else:
            beep(1000,500)
    elif is_silent and pt.isLinux():
        playAudio(tone)
    elif is_silent and pt.isTermux():
        if seq:
            vibrate(200)
        else:
            vibrate(800)
    else:
        playAudio(tone)