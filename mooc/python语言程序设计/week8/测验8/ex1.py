#ex1.py
txt = input()
for t in txt:
    if 'a' <= t <= 'z' or 'A' <= t <= 'Z':
        print(t, end="")