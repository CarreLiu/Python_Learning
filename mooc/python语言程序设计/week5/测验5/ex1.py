#ex1.py
import random

def genpwd(length):
    return random.randint(pow(10, length - 1), pow(10, length))

length = eval(input())
random.seed(17)
for i in range(3):
    print(genpwd(length))
