#ex1.py
str = input()
a = set(str)
sum = 0
for i in a:
    sum += eval(i)
print(sum)