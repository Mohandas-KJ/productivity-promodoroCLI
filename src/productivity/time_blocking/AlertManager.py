# This File maintains the CODE
# for user alerts

# Imports
from productivity.commons import platrad as pt
import os, subprocess
import threading
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
        print('Vibrator Error')

def playAudio(tid,seq):
    BASE_DIR = Path(__file__).resolve().parents[2]
    TONE_DIR = BASE_DIR / "assets" / "sounds"

    sound_map = {
        1: "digital_clock.wav",
        2: "doodle.wav",
        3: "london.wav",
        4: "techtonic.wav",
        5: "tick-tock.wav",
        6: "trap.wav"
    }

    sound_file = sound_map.get(tid)
    if not sound_file:
        return

    path_s = str(TONE_DIR / sound_file)

    try:
        if pt.isWindows():
            subprocess.Popen([
                "powershell",
                "-NoProfile",
                "-Command",
                f"(New-Object Media.SoundPlayer '{path_s}').PlaySync()"
            ])
        elif pt.isLinux():
            subprocess.Popen(['aplay',path_s],
                         stderr=subprocess.DEVNULL,
                         stdout=subprocess.DEVNULL)
        elif pt.isMac():
            subprocess.Popen(["afplay",path_s])
        elif pt.isTermux():
            if seq:
                vibrate(200)
            else:
                vibrate(800)
            os.system(f"termux-media-player play {path_s}")
    except Exception:
        print("\a",end="",flush=True)
        print('There is a Problem with your Sound Card')


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
        playAudio(tone,seq)