arr = [int(n) for n in input().split()]
a = arr[0]
b = arr[1]
m = arr[2]
x = arr[3]
list = []
result = ""
len = 10e6
next = []
for i in range(len):
    x = (x * a + b) % m
    result += str(x)
    # list.append(x)
    # q.put(x)
    # q.get()

print(result)


def getnex(str):
    i = 0
    j = -1
