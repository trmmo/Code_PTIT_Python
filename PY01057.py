import math

nOT = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def check(s):
    for i in range(len(s)):
        if isPrime(i):
            if not isPrime(int(s[i])):
                return False
        elif isPrime(int(s[i])):
            return False
    return True


for i in range(nOT):
    s = str(input())
    if check(s):
        print("YES")
    else:
        print("NO")
