nOT = int(input())
ls = []


def check(n):
    if len(n) % 2 == 1:
        return False
    for i in range(len(n)):
        if int(n[i]) % 2 == 1:
            return False
    return n == n[::-1]


def init(s, e):
    for i in range(s, e + 1):
        if check(str(i)):
            ls.append(i)


init(22, 100)
init(1000, 10000)
init(100000, 1000000)


for i in range(nOT):
    n = str(input())
    for j in ls:
        if j < int(n):
            print(j, end=" ")
        else:
            break
    print()
