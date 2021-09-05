n = int(input())
a = list(map(int, input().split()))
b = []
c = []
count = 0
st = 0
k = 0
for i in range(n):
    for j in range(n):
        if i != j and (str(j + 1) + ' ' + str(i + 1)) not in c:
            b.append(a[i] + a[j])
            c.append(str(i + 1) + ' ' + str(j + 1))
for i in b:
    if b.count(i) > count:
        count = b.count(i)
        summ = i
for i in range(len(b)):
    if b[i] == summ and k < n / 2:
        print(c[i])
        m = c[i].split()
        for j in range(len(c)):
            if m[0] == c[j].split()[0] or m[0] == c[j].split()[1] or m[1] == c[j].split()[0] or m[1] == c[j].split()[1]:
                b[j] = -14
        k += 1
