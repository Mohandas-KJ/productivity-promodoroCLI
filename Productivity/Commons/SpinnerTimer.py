import time,sys,itertools

def spintimer(seconds):
    spinner = itertools.cycle("|/-\\")
    for remaining in range(seconds,-1,-1):
        mins,secs = divmod(remaining,60)
        sym = next(spinner)
        sys.stdout.write(f"\r{sym}  {mins:02d}:{secs:02d}")
        sys.stdout.flush()
        time.sleep()
    sys.stdout.write("\033[2k\r")
    sys.stdout.flush()