#ex4.py
import jieba
f = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week10\\测验10\\沉默的羔羊.txt", encoding="utf-8").read()
counts = {}
txt = jieba.lcut(f)
for ch in txt:
    counts[ch] = counts.get(ch, 0)+1
maxn = 0
str = ""
for i in counts:
    if len(i) > 2 and counts[i] > maxn:
        str = i
        maxn = counts[i]
    elif counts[i] == maxn and i > str and len(i) > 2:
        str = i
print(str)