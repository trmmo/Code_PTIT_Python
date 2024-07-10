n, m = map(int, input().split())
ar = []
for _ in range(n):
    ar.append(list(map(int, input().split())))
if n > m:
    cnt = 0
    for _ in range(n):
        if _ % 2 == 0 and cnt < n - m:
            cnt += 1
            continue
        for __ in range(m):
            print(ar[_][__], end=" ")
        print()
else:
    for _ in range(n):
        cnt = 0
        for __ in range(m):
            if __ % 2 == 1 and cnt < m - n:
                cnt += 1
                continue
            print(ar[_][__], end=" ")
        print()
