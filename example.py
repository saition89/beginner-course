n = int(input())
a = []
b = [0] * n
k = 1
st = 0
for i in range(n):
    c = b.copy()
    a.append(c)
for h in range(n * 2):
    if h - st * 4 == 0:
        for i in range(st, n - st):
            a[0 + st][i] = k
            k += 1
    if h - st * 4 == 1:
        for i in range(1 + st, n - 1 - st):
            a[i][n - 1 - st] = k
            k += 1
    if h - st * 4 == 2:
        for i in range(n - 1 - st, 0 + st, -1):
            a[n - st - 1][i] = k
            k += 1
    if h - st * 4 == 3:
        for i in range(n - st - 1, 0 + st, -1):
            a[i][0 + st] = k
            k += 1
        st += 1
for i in range(n):
    print(' '.join(list(map(str, a[i]))))
    print()
