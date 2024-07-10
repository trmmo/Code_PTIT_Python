import math

nOT = int(input())


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def digitSum(a):
    s = 0
    while a != 0:
        s += a % 10
        a //= 10
    return s


def is_Prime(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return a > 1


for i in range(nOT):
    ar = str(input()).split(" ")
    n = int(ar[0])
    m = int(ar[1])
    a = gcd(n, m)
    # print(dsts, digitSum(dsts))
    if is_Prime(digitSum(a)):
        print("YES")
    else:
        print("NO")