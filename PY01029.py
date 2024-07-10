nOT = int(input())


def gcd(a, b):
    while  b != 0:
        r = a % b
        a = b
        b = r
    return a


for i in range(nOT):
    n = int(input())
    s = str(n)
    n1 = int(s[::-1])
    if gcd(n, n1) == 1:
        print("YES")
    else:
        print("NO")
