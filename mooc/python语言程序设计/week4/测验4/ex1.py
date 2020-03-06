#ex1.py
for i in range(1000, 10000):
    s = str(i)
    if (eval(s[0]) ** 4 + eval(s[1]) ** 4 + eval(s[2]) ** 4 + eval(s[3]) ** 4) == i:
        print(i)