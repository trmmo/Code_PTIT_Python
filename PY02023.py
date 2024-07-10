t = int(input())


def digitsum(n):
    s = 0
    st = str(n)
    for i in range(len(st)):
        s += int(st[i])
    return s


for _ in range(t):
    n = int(input())
    ar = list(map(int, input().split()))
    ar2 = []
    # ar.sort()
    # print(ar)
    for i in range(n):
        ar2.append(digitsum(ar[i]))
    print(ar2)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if ar2[i] > ar2[j]:
                tmp = ar2[i]
                ar2[i] = ar2[j]
                ar2[j] = tmp
                tmp2 = ar[i]
                ar[i] = ar[j]
                ar[j] = tmp2
    print(ar)
