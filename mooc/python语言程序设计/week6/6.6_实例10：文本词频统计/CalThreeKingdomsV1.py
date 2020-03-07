#CalThreeKingdomsV1.py
import jieba
txt = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week6\\6.6_实例10：文本词频统计\\threeKingdoms.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))