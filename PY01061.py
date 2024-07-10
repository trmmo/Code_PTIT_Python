import math

nOT = int(input())


def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n > 1


def check(s):
    if not isPrime(len(s)):
        return False
    pc = 0
    nc = 0
    for i in range(len(s)):
        if isPrime(int(s[i])):
            pc += 1
        else:
            nc += 1
    if nc >= pc:
        return False
    return True


for i in range(nOT):
    s = str(input())
    if check(s):
        print("YES")
    else:
        print("NO")
