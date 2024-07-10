n = int(input())
ls = []

for i in range(n):
    tmp = list(map(int, input().split()))
    ls.append(tmp)

k = int(input())

d1 = 0
d2 = 0
for i in range(n):
    for j in range(n):
        if i < j: d1 += ls[i][j]
        if i > j: d2 += ls[i][j]

if abs(d1 - d2) <= k:
    print("YES")
else:
    print("NO")
print(abs(d1 - d2))