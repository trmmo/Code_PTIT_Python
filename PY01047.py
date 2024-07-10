import math

nOT = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


for i in range(nOT):
    s = str(input())
    n = int(s[-4:])
    if isPrime(n):
        print("YES")
    else:
        print("NO")
