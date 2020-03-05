#ex5_ans.py
s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z':
        t += chr((ord(c) - ord('a') + 3) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        t += chr((ord(c) - ord('A') + 3) % 26 + ord('A'))
    else:
        t += c
print(t)