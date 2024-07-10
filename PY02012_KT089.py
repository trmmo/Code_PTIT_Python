t = int(input())
ar = list(map(int, input().split()))
while len(ar) < t:
    ar.extend(list(map(int, input().split())))

ols = []
els = []

for i in ar:
    if i % 2 == 0:
        els.append(i)
    else:
        ols.append(i)
els.sort(reverse=True)
ols.sort()
# for i in range()
# print(els)
# print(ols)
res = []
for i in ar:
    if i % 2 == 0:
        res.append(els.pop())
    else:
        res.append(ols.pop())
for i in res:
    print(i, end=" ")