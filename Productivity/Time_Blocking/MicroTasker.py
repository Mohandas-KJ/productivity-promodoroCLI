import os
import time
import Productivity.Commons.TimeSheet as ts
import Productivity.Time_Blocking.MTTimer as timer

#To give Intro about the technique
def About():
    print("Micro-Tasking: \nMicro-Tasking is a high-efficiency productivity method where work is broken into rapid 2–5 minute tasks, " \
    "completed back-to-back without scheduled breaks. It eliminates procrastination by making every task too small to resist, " \
    "creating effortless momentum and deep focus. This system enables fast context switching, sustained energy, and extreme output — " \
    "perfect for modern developers and learners.\n")

def Configure():
    os.system('cls')
    About()
    print('Configuration: ')
    Num_of_tasks = int(input('Enter Number of Tasks: '))
    Time_per_task = int(input('Enter Time per Task: '))
    hrs,mins = ts.getTotal(Num_of_tasks, Time_per_task)
    print(f'\nTotal Time: {hrs} {'Hours' if hrs > 1 else 'Hour'} {mins} Minutes')

    #Task Entry
    tasks = []
    print('\nTask Entry: ')
    for i in range(Num_of_tasks):
        tasks.append(input(f'Task {i+1}: '))
    
    return Num_of_tasks,Time_per_task,tasks
    
def Scedule():
    Total_loop,tick,tasks = Configure()
    os.system('cls')
    target = len(tasks)
    count  = 0
    timer.execute_task(tasks,tick)



