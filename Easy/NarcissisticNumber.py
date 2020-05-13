import numpy as np


def isNarcissisticNumber(n):
    origin = n
    sum = 0
    while n > 0:
        tmp = n % 10
        # print("tmp=",tmp)
        sum += np.power(tmp, 3)
        # print("sum=",sum)
        n = int(n / 10)
        # print("n=",n)

    if sum == origin:
        return True
    else:
        return False


# print(isNarcissisticNumber(153))
arr = [int(n) for n in input().split()]
for i in range(arr[0], arr[1]):
    if isNarcissisticNumber(i):
        print(i, " ", end="")
