n = int(input())
ar = [int(x) for x in input().split()]
ar.sort()
# print(ar)
res = []
res.append(ar[-3] * ar[-2] * ar[-1])
res.append(ar[0] * ar[2] * ar[1])
res.append(ar[0] * ar[-2] * ar[-1])
res.append(ar[1] * ar[0] * ar[-1])
res.append(ar[-2] * ar[-1])
res.append(ar[0] * ar[1])
res.append(ar[0] * ar[-1])
print(max(res))
