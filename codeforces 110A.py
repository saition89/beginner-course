n = list(map(int, ' '.join(input().split())))
k = n.count(4)
m = n.count(7)
if k + m == 7 or k + m == 4:
    print('YES')
else:
    print('NO')
