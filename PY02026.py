n, m = map(int, input().split())
a1 = [int(x) for x in input().split()]
a2 = [int(x) for x in input().split()]
s1 = set(a1)
s2 = set(a2)
if s1 == s2:
    print("YES")
else:
    print("NO")