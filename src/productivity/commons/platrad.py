# This file Contains the essentials for OS Detection
import platform
import os

def isWindows():
    if platform.system == "Windows":
        return True
    
def isLinux():
    if platform.system == "Linux":
        return True

def isTermux():
    if "ANDROID_ROOT" in os.environ or "com.termux" in os.environ.get("TERM",""):
        return True

