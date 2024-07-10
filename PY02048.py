n, k = map(int, input().split())
ar = [int(x) for x in input().split()]
ar.sort()
cnt = 1
for i in range(1, n):
    if abs(ar[i] - ar[i - 1]) > k:
        cnt += 1
print(cnt)
