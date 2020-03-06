#ex3.py
def cmul(*b):
    m = 1
    for i in b:
        m *= i
    return m

c = "cmul({})".format(input())#将input()的值原封不动的加到前面的{}并且不带引号
print(eval(c))