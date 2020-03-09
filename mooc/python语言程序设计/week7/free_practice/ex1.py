#ex1.py
txt = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\free_practice\\latex.log", "r")
count = 0
for line in txt:
    if line != "\n":
        count += 1
print("共{}行".format(count))