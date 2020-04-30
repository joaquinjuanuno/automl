import time
import sys

spaces = " " * position
for position in range(50):
    with open(f'drawings/{sys.argv[1]}.txt') as f:
        object_ = f.read().strip()
    print(f'{spaces}{object_}', end='\r')
    time.sleep(.x2)
