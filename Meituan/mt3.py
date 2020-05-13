arr1 = [int(n) for n in input().split()]
n = arr1[0]
k = arr1[1]

arr2 = [int(n) for n in input().split()]

arr = sorted(arr2)

if k % len(arr) == 0:
    zu = k / len(arr)
    yu = len(arr)
    print("(" + str(arr[zu - 1]) + "," + str(arr[-1]) + ")")

else:
    zu = k // len(arr)
    yu = k % len(arr)
    print("(" + str(arr[zu]) + "," + str(arr[yu - 1]) + ")")
