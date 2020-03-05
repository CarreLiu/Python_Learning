#ex3.py
total = 0
for i in range(1, 967):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(total)