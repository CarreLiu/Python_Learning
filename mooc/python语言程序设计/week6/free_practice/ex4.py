#ex4.py
words = eval(input())
ans = {}
if type(words) != dict:
    print("输入错误")
else:
    for word in words:
       ans[words[word]] = word 
    print(ans)