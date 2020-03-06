#ex2.py
from math import sqrt
counts = 2
for i in range(3, 101, 2):
    mid = int(sqrt(i))
    for j in range(2, mid + 1):
        if i % j == 0:
            break
    else:
        counts += i
print(counts)