def InsertSort(arr):
    for i in range(0, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            # 一个一个移动
            if arr[j] > key:
                arr[j + 1] = arr[j]
                arr[j] = key
            j -= 1
            # print(arr)
        # print(arr)
    return arr


arr = [5, 1, 2, 3, 8, 7, 4, 9]
print(InsertSort(arr))
