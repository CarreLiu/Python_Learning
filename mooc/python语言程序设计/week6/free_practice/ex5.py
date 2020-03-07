import jieba
txt = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week6\\free_practice\\沉默的羔羊.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
ans = ""
maxn = 0
for i in counts:
    if counts[i] > maxn and len(i) > 2:
        ans = i
        maxn = counts[i]
    elif counts[i] == maxn and i > ans:
        ans = i
print(ans)