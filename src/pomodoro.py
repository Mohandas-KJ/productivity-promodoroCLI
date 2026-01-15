#This is the Main Program where manny Productivity Techniques are included
#Imports (Library and Modules)
import time
import sys
import argparse
from productivity.time_blocking import micro_tasker as ms # Done imports wrongly. Following up with right one!

# Argument Parser
def a_parser():
    pars = argparse.ArgumentParser(
        description="Pomodoro CLI - Productivity CLI Timer"
    )

    #Silent arg
    pars.add_argument("--silent",action="store_true",
                      help="Disable sound alerts")
    
    #tone arg
    pars.add_argument("--tone",type=int,default=1,
                      help="Choose tone flavour")
    
    return pars.parse_args()

program_args = a_parser() # Get user args

def start():
    print('Welcome to Promodoro CLI!')
    print('\nChoose Your Productivity Method: ')
    print('1. Micro Time Blocking (Musk\'s Method)\n')
    print('That\'s all for now!')

    choice = int(input('Choice: '))

    match(choice):
        case 1:
            ms.Scedule(program_args.silent,program_args.tone)
        case _:
            print('Please choose the appropriate one!')

if __name__ == "__main__":
    start()