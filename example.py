r, c = map(int, input().split())
a = []
R = []
C = []
count = 0
restr = 0
for i in range(r):
    b = ' '.join(input()).split()
    for j in range(c):
        if b[j] == 'S':
            R.append(i)
            C.append(j)
    a.append(b)
for i in range(c):
    if i not in C:
        count += r
        restr += 1
for i in range(r):
    if i not in R:
        count += c - restr
print(count)
