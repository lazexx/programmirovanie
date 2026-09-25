n = int(input())
result = list()
a = list(range(n + 1))
a[0] = a[1] = 0
for m in range(2, n + 1):
    if a[m] != 0:
        for j in range(m * 2, n + 1, m):
            a[j] = 0
for i in range(2, n + 1):
    if a[i] != 0:
        result.append(i)
print(result)