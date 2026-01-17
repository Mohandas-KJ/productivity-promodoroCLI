# This file Contains the essentials for OS Detection
import platform
import os

def isWindows():
    if platform.system() == "Windows":
        return True
    else:
        return False
    
def isLinux():
    if platform.system() == "Linux":
        return True
    else:
        return False

def isTermux():
    if "ANDROID_ROOT" in os.environ or "com.termux" in os.environ.get("TERM",""):
        return True
    else:
        return False

def isMac():
    if platform.system() == "Darwin":
        return True
    else:
        return False

def Clear_Screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')