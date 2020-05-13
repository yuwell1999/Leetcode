import math
import numpy as np


def getLayer(x):
    return int(math.log2(x)) + 1


def dev(x):
    return x // 2


def calc(x, k):
    if k >= getLayer(x):
        return -1

    for i in range(1, getLayer(x) - k + 1):
        x = dev(x)
    return x


Q = int(input())

mat = np.zeros((Q, 2), dtype=int)

# print(calc(2**31-1,3))
for i in range(Q):
    mat[i][0], mat[i][1] = [int(n) for n in input().split()]

for i in range(Q - 1):
    print(calc(mat[i][0], mat[i][1]))

print(calc(mat[Q - 1][0], mat[Q - 1][1]), end='')