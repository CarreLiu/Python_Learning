#ex4.py
n = eval(input())
str = "*"
for i in range(1, n + 1, 2):
    print("{0:^{1}}".format(str * i, n))