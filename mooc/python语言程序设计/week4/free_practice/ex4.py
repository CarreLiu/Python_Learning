#ex4.py
flag = False
for i in range(100, 1000):
    temp = i
    total = 0
    for j in range(2, -1, -1):
        total += (temp // pow(10, j)) ** 3
        temp %= pow(10, j)
    if total == i:
        if flag == True:
            print(",", end="")
        print("{}".format(i), end="")
        flag = True