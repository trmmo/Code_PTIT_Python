import math

n = int(input())
ar = [int(x) for x in input().split()]


def isprime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return x > 1


ar = list(dict.fromkeys(ar))
n = len(ar)

# print(ar)
# print(n)
# bl = True
# for _ in range(n - 1):
#     s1 = 0
#     for i in range(0, _ + 1):
#         s1 += ar[i]
#     if isprime(s1):
#         s2 = 0
#         for j in range(_ + 1, n):
#             s2 += ar[j]
#         if isprime(s2):
#             print(_)
#             break
#         else:
#             bl = False
#     else:
#         bl = False
# if not bl:
#     print("NONE")
ok = 0
for i in range(1, n) : ar[i] += ar[i - 1]
for i in range(n) :
    if isprime(ar[i]) and isprime(ar[n - 1] - ar[i]) :
        ok = 1
        print(i)
        break
if ok == 0 : print("NOT FOUND")
