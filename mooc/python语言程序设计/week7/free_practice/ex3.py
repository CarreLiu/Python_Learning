#ex3.py
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week7\\free_practice\\latex.log", "r")
counts = {}
for line in f:
    counts[line] = counts.get(line, 0)+1
txt = list(counts.items())
txt.sort(key=lambda x : x[1])
total = 0
for i in range(len(txt)):
    word, nums = txt[i]
    if nums != 1:
        break
    total += 1
print("共{}独特行".format(total))