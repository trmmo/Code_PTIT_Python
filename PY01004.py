import math

nOT = int(input())


def is_Prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return a > 1


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


for i in range(nOT):
    n = int(input())
    cnt = 0
    for j in range(1, n):
        if gcd(n, j) == 1:
            cnt += 1
    # print(cnt)
    if is_Prime(cnt):
        print("YES")
    else:
        print("NO")
    