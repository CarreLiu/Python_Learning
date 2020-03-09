#ex4.py
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\free_practice\\data.csv")
for line in f:
    line = line.strip("\n")
    ls = line.split(",")
    ls = ls[::-1]
    print(",".join(ls))
f.close()