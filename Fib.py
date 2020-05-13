ans = [1, 1]

for i in range(3, pow(10, 3)):
    ans.append(ans[-1] + ans[-2])

print(ans)
