import math

nOT = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

for i in range(nOT):
    s = str(input())
    t = 0
    for j in range(len(s)):
        t += int(s[j])
    if isPrime(t):
        print("YES")
    else:
        print("NO")
