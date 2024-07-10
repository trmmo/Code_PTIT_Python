import math

nOT = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


def check(s):
    t = 0
    for i in range(len(s)):
        t += int(s[i])
    if not isPrime(t):
        return False
    for i in range(len(s)):
        if (i % 2) != (int(s[i]) % 2):
            return False
    return True


for i in range(nOT):
    s = str(input())
    if check(s):
        print("YES")
    else:
        print("NO")
