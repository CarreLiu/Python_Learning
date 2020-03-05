#ex1.py
def dayUp(df):
    dayup =  1
    for i in range(365):
        if i % 7 in [6, 0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
a = 1
for i in range(365):
    a = a * (1 + 0.01)
factor = 0.01
while dayUp(factor) < a:
    factor += 0.001
print("工作日的努力参数是: {:.3f}".format(factor))