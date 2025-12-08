#This is the Main Program where manny Productivity Techniques are included
#Imports (Library and Modules)
import time
import Productivity.Time_Blocking.MicroTasker as ms

def start():
    print('Welcome to Promodoro CLI!')
    print('\nChoose Your Productivity Method: ')
    print('1. Micro Time Blocking (Musk\'s Method)\n')
    print('That\'s all for now!')

    choice = int(input('Choice: '))

    match(choice):
        case 1:
            ms.Scedule()
        case _:
            print('PLease choose the appropriate one!')

if __name__ == "__main__":
    start()