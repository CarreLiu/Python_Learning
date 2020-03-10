#ex3.py
try:
    txt = eval(input())
    e = {}
    for i in txt:
        e[txt[i]] = i
    print(e)
except:
    print("输入错误")