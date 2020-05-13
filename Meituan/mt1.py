l = [int(n) for n in input().split()]
m = l[0]
n = l[1]

import numpy as np

mat = np.zeros((n, m), dtype=int)

for i in range(n):
    for j in range(m):
        mat[i][j] = int(input())

print(mat)
