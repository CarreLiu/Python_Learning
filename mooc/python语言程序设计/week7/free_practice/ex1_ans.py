#ex1.py
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\free_practice\\latex.log", "r")
s = 0
for line in f:
    line = line.strip("\n")
    if len(line) == 0:
        continue
    s += 1
print("共{}行".format(s))