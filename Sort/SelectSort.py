def SelectSort(arr):
    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


arr = [2, 1, 3, 4, 5, 7, 0]
print(SelectSort(arr))
