n, m = map(int, input().split())
listq = []
p = 0
for i in range(n * m):
    if i < 10:
        listq.append(' ' + str(i))
    else:
        listq.append(str(i))
for i in range(n):
    lista = listq[p:(p + m)]
    if (p // m) % 2 == 0:
        print(' '.join(lista))
    else:
        lista.reverse()
        print(' '.join(lista))
    print()
    p += m
