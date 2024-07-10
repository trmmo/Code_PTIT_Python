import math

n = int(input())

ar = list(map(int, input().split()))
# res = []
ar.sort()
for i in range(0, n - 1):
    for j in range(i + 1, n):
        tmp = []
        if math.gcd(ar[i], ar[j]) == 1:
            print(ar[i], ar[j])
        # res.append(tmp)
# for i in res:
#     for j in i:
#         print(j, end=" ")
#     print()
