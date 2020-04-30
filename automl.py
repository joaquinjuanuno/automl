import time
import sys

for position in range(50):
    with open('drawings/esloch.txt') as f:
        object_ = f.read().strip()
    print(f'{" " * position}{object_}', end='\r')
    time.sleep(.1)
