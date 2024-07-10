import math

n, m = list(map(int, input().split()))
mt = []


def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


for i in range(n):
    mt.append(list(map(int, input().split())))

for i in mt:
    for j in i:
        if isPrime(j):
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
