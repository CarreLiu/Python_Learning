#CalStatisticsV1.py
def getNum():       #获取用户不定长度的输入
    num = eval(input())
    return num

def mean(numbers):  #计算平均值
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)
    
def dev(numbers, mean): #计算标准差
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers)-1), 0.5)

def median(numbers):    #计算中位数
    num = sorted(numbers)
    if len(num) % 2 == 0:
        med = (num[len(num)//2-1] + num[len(num)//2]) / 2
    else:
        med = num[(len(num)-1)//2]
    return med
    
n =  getNum() #主体函数
m =  mean(n)
print("平均值:{:.2f},标准差:{:.2f},中位数:{}".format(m, dev(n, m), median(n)))
