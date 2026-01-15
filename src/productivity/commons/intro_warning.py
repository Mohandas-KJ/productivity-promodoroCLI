# This is for Notifing User
# Based on the arguments passed

# Imports
import time
from productivity.commons import platrad as pt

def Warning(is_silent):
    if is_silent and pt.isWindows():
        print('Warning: Silent Mode Active! System will use short-beep for reminders')
        time.sleep(3)
        pt.Clear_Screen()
    elif is_silent and pt.isLinux():
        print('Warning: Silent mode is not supported in Linux Yet! System will use the default tone')
        time.sleep(3)
        pt.Clear_Screen()
    elif is_silent and pt.isTermux():
        print('Warning: Silent Mode Active! Android will vibrate for reminders')
        time.sleep(3)
        pt.Clear_Screen()