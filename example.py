n, m = map(int, input().split())
list_a = []
b = 0
for i in range(n):
    list_b = input().split()
    list_a.append(list_b)
for i in range(n):
    if 'C' in list_a[i] or 'M' in list_a[i] or 'Y' in list_a[i]:
        print('#Color')
        break
    else:
        b += 1
if b == n:
    print('#Black&White')
