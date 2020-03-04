#MathCalc
str = input()
if str[0] == '-':
    begin = 1
    count = 1
else:
    begin = 0
    count = 0
for c in str[begin:]:
    if c in [' ', '+', '-', '*', '/']:
        break
    count = count + 1
m = eval(str[:count])
count2 = count
for c in str[count:]:
    if c in ['+', '-', '*', '/']:
        op = c
        break
    count2 = count2 + 1
count2 = count2 + 1
count = count2
for c in str[count2:]:
    if c not in [' ']:
        break
    count = count + 1
n = eval(str[count:])

if op == '+':
    print("{:.2f}".format(m+n))
elif op == '-':
    print("{:.2f}".format(m-n))
elif op == '*':
    print("{:.2f}".format(m*n))
else:
    print("{:.2f}".format(m/n))