import random
import time
import time
import os
clear = lambda: os.system('cls')

def roll(min, max):
     result = random.randint(min, max)
     return result


rzut = roll(1,6)

def kosc():
    for n in range(rzut - 1):
        print(".")
        time.sleep(0.5)
    print(rzut)

kosc()

