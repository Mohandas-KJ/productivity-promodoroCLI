import Productivity.Commons.SpinnerTimer as stimer
import winsound,threading,sys
import Productivity.Time_Blocking.MicroTasker as mt

count = 0

def execute_task(tasks,target,per_task):
    global count

    if count == target:
        print('\nCONGRADULATIONS JOB DONE!')
        return
    
    temp = tasks.pop(0)

    winsound.Beep(1000,500)
    print(f'Current Tasks: {temp}')
    stimer.spintimer(per_task)
    count+=1
    print(f'Completed: {temp}')
    winsound.Beep(1500,700)

    if count < target:
        threading.Timer(2,execute_task,args=(tasks,target,per_task)).start()
    else:
        print('\nCONGRADULATIONS JOB DONE!')
