#ex2.py
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week10\\测验10\\latex.log")
counts = {}
for line in f:
    counts[line] = counts.get(line, 0) + 1
print("共{}关键行".format(len(counts)))