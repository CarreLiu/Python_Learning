#ex2.py
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\free_practice\\latex.log", "r")
total = 0
count = {}
for line in f:
    for i in line:
        total += 1
        if 'a' <= i <= 'z':
            count[i] = count.get(i, 0) + 1
txt = list(count.items())
txt.sort(key=lambda x: x[0])
print("共{}字符".format(total), end="")
for i in range(len(txt)):
    word, nums = txt[i]
    print(",{}:{}".format(word, nums), end="")