alpha = []
for i in range(26):
    alpha.append(chr(ord('a')+i))
    alpha.append(chr(ord('A')+i))
s = input()
for c in s:
    if c in alpha:
        print(c, end="")