n, m = map(int, input().split())
a = []
b = ['.'] * (n + 2)
a.append(b)
count = 0
for i in range(n):
    c = ' '.join('.' + input() + '.').split()
    a.append(c)
a.append(b)
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i][j] == '.':
            if a[i][j - 1] == '.' and a[i - 1][j] == '.' and a[i][j + 1] == '.' and a[i + 1][j] == '.':
                count += 1
    print(count)
