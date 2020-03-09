#ex2.py
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\测验7\\data.csv")
list = []
for line in f:
    line = line.strip("\n")
    line = line.replace(" ", "")
    line = line.replace(",", ";")
    line = line[::-1]
    list.insert(0, line)
for i in list:
    print(i)