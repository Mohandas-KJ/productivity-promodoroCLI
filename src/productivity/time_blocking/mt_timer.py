from productivity.commons import spinner_timer as stimer
import threading,sys,platform,os,time

#Cross-platform Beep helper
def beep(frequency, tp_ms,vibration):

    #Check if Windows and Play the sound
    try:
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(frequency,tp_ms)
            return
    except Exception:
        pass

    #Additional Vibration feature if it's on Andoid's Termux
    try:
        if "ANDROID_ROOT" in os.environ or "com.termux" in os.environ.get("TERM",""):
            os.system(f"termux-vibrate -d {vibration}")
            return
    except Exception:
        pass

    #Fallback, if none is possible
    print("\a",end="",flush=True)

def execute_task(tasks, target, time_per_task, is_silent, tone, interval_time=2, run_async=False):

    def worker():
        if target != len(tasks):
            pass

        #To keep Count on the Completed
        completed = 0
    
        #The Timer Loop
        while tasks:
            temp = tasks.pop(0)

            #Play a Sound
            try:
                beep(1500,700,200)
            except Exception:
                pass

            #Display Ongoing Task
            print(f'Current Task: {temp}')

        #Handle SpinTimer
            try:
                stimer.spintimer(time_per_task)
            except Exception as e:
                print(f'\nSpin Timer Failed: {e}')
                time.sleep(time_per_task)
        
            completed += 1
            print(f'Completed: {temp} ({completed}/{target})')
            try:
                beep(1000,500,800)
            except Exception:
                pass
        
            if interval_time and tasks:
               time.sleep(interval_time)
    
        print("\nCONGRADULATIONS JOB DONE!")

    if run_async:
        t = threading.Thread(target=worker,daemon=True)
        t.start()
        return t
    else:
        worker()
        return None





