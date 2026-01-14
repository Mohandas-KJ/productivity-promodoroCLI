# This file is created to simulate the `run.py` file
import argparse
import subprocess
import sys

# The Run Command template
cmd = [sys.executable, "st/mn.py"]

# forward any additional CLI args (skip argv[0])
if len(sys.argv) > 1:                                # Always 1 because of the file name || If any forward to th main file `mn.py` (Here)
	cmd.extend(sys.argv[1:]) 

subprocess.run(cmd)