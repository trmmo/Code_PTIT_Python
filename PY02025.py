n, m = map(int, input().split())
ar1 = [int(x) for x in input().split()]
ar2 = [int(x) for x in input().split()]
c, d = {}, {}
for i in ar1: c[i] = 1
for i in ar2: d[i] = 1

for i in sorted(list(c)) :
    if i in d : print(i, end = ' ')
print()
for i in sorted(list(c)) :
    if not(i in d) : print(i, end = ' ')
print()
for i in sorted(list(d)) :
    if not(i in c) : print(i, end = ' ')
