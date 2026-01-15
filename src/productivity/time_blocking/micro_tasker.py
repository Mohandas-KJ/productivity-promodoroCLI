import os
import time, platform
from productivity.commons import time_sheet as ts
from productivity.time_blocking import mt_timer as timer

#To give Intro about the technique
def About():
    print("Micro-Tasking: \nMicro-Tasking is a high-efficiency productivity method where work is broken into rapid 2–5 minute tasks, " \
    "completed back-to-back without scheduled breaks. It eliminates procrastination by making every task too small to resist, " \
    "creating effortless momentum and deep focus. This system enables fast context switching, sustained energy, and extreme output — " \
    "perfect for modern developers and learners.\n")

def Configure():
    Clear_Screen()
    About()
    print('Configuration: ')

    Num_of_tasks = None
    Time_per_task = None

    while True:
        try:
            Num_of_tasks = int(input('Enter Number of Tasks: '))
            Time_per_task = int(input('Enter Time per Task (min): '))
            if Num_of_tasks <= 0 or Time_per_task <= 0:
                print('Values must be greater than zero!\n')
                continue
            break
        except ValueError:
            print('Only Integer values are allowed!\n')

    hrs,mins = ts.getTotal(Num_of_tasks, Time_per_task)
    print(f'\nTotal Time: {hrs} {'Hours' if hrs > 1 else 'Hour'} {mins} Minutes')

    #Task Entry
    tasks = []
    print('\nTask Entry: ')
    for i in range(Num_of_tasks):
        tasks.append(input(f'Task {i+1}: '))
    
    return Num_of_tasks,Time_per_task,tasks
    
def Scedule(is_silent,tone):
    Total_loop,tick,tasks = Configure()
    Clear_Screen()
    target = len(tasks)
    print('Timer Started. Stay Focused!\n')
    timer.execute_task(tasks.copy(),target,tick*60,is_silent,tone)

def Clear_Screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')



