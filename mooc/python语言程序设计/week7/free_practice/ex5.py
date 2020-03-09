#ex5.py
#ex4.py
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\free_practice\\data.csv")
s = f.read()
s = s.replace(" ", "")
print(s)
f.close()