import math

n = int(input())
ar = list(map(int, input().split()))


def isprime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


d = {}
for i in ar:
    if isprime(i):
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] +=1
for k, v in d.items():
    print(k, v)
