def summand1(list1):
    if len(list1) == 1:
        return 1
    elif (len(list1) % 2 == 0 and list1[0] == list1[-1]) or len(list1) == 2 or list1[-1] + list1[-2] > list1[0]:
        list2 = [1] * (x - list1[0])
        list2[0] = list1[0] + 1
        list1 = list2.copy()
        print(list1)
    elif len(list1) % 2 != 0 and list1[0] == list1[-2] or list1[-1] + list1[-2] > list1[0]:
        list2 = [1] * (x - list1[0])
        list2[0] = list1[0] + 1
        list1 = list2.copy()
        print(list1)
    else:
        p = len(list1)
        for i in range(1, p-1):
            if i == p:
                break
            list1[i] += 1
            list1[-1] += -1
            if 0 in list1:
                list1.remove(0)
            p = len(list1)
            print(list1)

    summand1(list1)


x = int(input())
LIST = [1] * x
list1 = LIST.copy()
print(list1)
summand1(list1)
