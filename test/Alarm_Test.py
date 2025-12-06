import threading

tasks = ['Task 1','Task 2','Task 3']

target = len(tasks)
count = 0

def execute_task():
    global count
    if count >= target:
        return
    print(f'Current Task: {tasks.pop(0)}')
    count += 1
    if count < target:
        threading.Timer(2, execute_task).start()

# start the repeating task once; the timer will reschedule as needed
execute_task()