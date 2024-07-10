s1 = input().lower()
s2 = input().lower()

set1 = set(s1.split())
set2 = set(s2.split())

inter = list(set1.intersection(set2))
inter.sort()
union = list(set1.union(set2))
union.sort()
for i in union:
    print(i, end=" ")
print()
for i in inter:
    print(i, end=" ")
