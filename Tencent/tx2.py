import operator
from functools import reduce

N, K = [int(n) for n in input().split()]

# mat = np.zeros((N, K),dtype=int)
mat = []
for i in range(N):
    arr = [int(n) for n in input().split()]
    del arr[0]
    mat.append(arr)

arr = reduce(operator.add, mat)
arr1 = sorted(arr, reverse=True)
# print(arr)
for i in range(K - 1):
    print(arr1[i], end='')
    print(' ', end='')

print(arr1[K - 1], end='')
