#ex2.
from math import ceil
def prime(m):
    for i in range(2, m):
        if m % i == 0:
            return False
    return True

n = eval(input())
n = ceil(n)
s = ""
count = 0
while count < 5:
    if prime(n):
        s = s + "{},".format(n)
        count += 1
    n += 1
print(s[:-1])