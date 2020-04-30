import time
import sys


for position in range(50):
    with open(f'drawings/{sys.argv[1]}.txt') as f:
        object_ = f.read().strip()
    spaces = " " * position
    print(f'{spaces}{object_}', end='\r')
    time.sleep(.1)
