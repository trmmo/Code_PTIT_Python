import math

a, b = list(map(int, input().split()))
for i in range (a, b - 1):
    for j in range (i + 1, b):
        for k in range (j + 1, b + 1):
            if math.gcd(i, j) == 1 and math.gcd(k, i) == 1 and math.gcd(j, k) == 1:
                print("(" + str(i) + ", " + str(j) + ", " + str(k)+ ")")
