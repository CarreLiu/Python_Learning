#ex2.py
import random
darts = eval(input())
hits = 0
random.seed(123)
for i in range(darts):
    x, y = random.random(), random.random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1:
        hits += 1
pi = 4 * hits / darts
print("{:.6f}".format(pi))