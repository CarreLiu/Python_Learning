#CalHamletV1.py
def getText():
    txt = open("D:\\GitHub\\Repositories\\Python_Learning\\mooc\\python语言程序设计\\week6\\6.6_实例10：文本词频统计\\hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}·~‘’':
        txt = txt.replace(ch, " ")
    return txt

hamletTxt = getText()
words = hamletTxt.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))