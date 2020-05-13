def BubbleSort(arr):
    for i in range(len(arr) - 1):
        flag = False

        for j in range(len(arr) - i - 1):  # 大的放到最后了

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True

        print("第" + str(i + 1) + "次排序的结果：" + str(arr))

        if flag:
            return arr

    return arr


# arr = [2, 4, 5, 1, 3, 8, 6, 0]
arr = [9, 1, 2, 3, 4, 5, 6, 7]

print(BubbleSort(arr))
