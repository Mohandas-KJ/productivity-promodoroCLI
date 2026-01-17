from productivity.commons import spinner_timer as stimer
from productivity.time_blocking.AlertManager import Alert
import threading,sys,platform,os,time

def execute_task(tasks, target, time_per_task, is_silent, tone, interval_time=10, run_async=False):

    def worker():
        if target != len(tasks):
            pass

        #To keep Count on the Completed
        completed = 0
    
        #The Timer Loop
        while tasks:
            temp = tasks.pop(0)

            #Play a Sound
            Alert(is_silent,tone,1)

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

            Alert(is_silent,tone,0)
        
            if interval_time and tasks:
               time.sleep(interval_time)
    
        print("\nCONGRADULATIONS JOB DONE!")

    if run_async:
        t = threading.Thread(target=worker,daemon=False)
        t.start()
        t.join()
        return t
    else:
        worker()
        return None





