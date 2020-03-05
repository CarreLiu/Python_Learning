#ex5.py
str = input()
for c in str:
    num = ord(c)
    if num >= 65 and num <= 90:
        num = (num - 65 + 3) % 26 + 65
        print("{}".format(chr(num)), end="")
    elif num >= 97 and num <= 122:
        num = (num - 97 + 3) % 26 + 97
        print("{}".format(chr(num)), end="")
    else:
        print(c, end="")