#HelloWorld
str = "Hello World"
count = 0
a = eval(input())
if a == 0:
    print(str)
elif a > 0:
    for c in str:
        print(c, end="")
        count = count+1
        if count % 2 == 0:
            print()
else:
    for c in str:
        print(c)