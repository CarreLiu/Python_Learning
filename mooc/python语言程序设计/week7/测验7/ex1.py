#ex1.py
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\测验7\\latex.log")
counts = 0
rows = 0
for line in f:
    line = line.strip("\n")
    counts += len(line)
    if (line != ""):
        rows += 1
ans = counts / rows
print(int(ans))
