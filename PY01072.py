n, k = map(int, input().split())
ls = list(map(int, input().split()))
ar = []
for i in ls:
    if i not in ar:
        ar.append(i)
ar.sort()
n = len(ar)
a = []


def Try(idx):
    if len(a) == k:
        for j in a:
            print(j, end=' ')
        print()
        return
    if idx == n:
        return
    for i1 in range(idx, len(ar)):
        a.append(ar[i1])
        Try(i1 + 1)
        a.pop()


Try(0)
