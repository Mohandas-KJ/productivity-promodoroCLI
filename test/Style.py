import time, sys, itertools

def spinner_timer(seconds):
    spinner = itertools.cycle("|/-\\")
    for remaining in range(seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        sym = next(spinner)
        sys.stdout.write(f"\r{sym}  {mins:02d}:{secs:02d}")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\033[2K\r")
    sys.stdout.flush()

    print("Done!")

spinner_timer(10)
