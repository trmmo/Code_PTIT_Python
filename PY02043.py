n = int(input())
for _ in range(n):
    s = input()
    t = input()
    cnt = 0
    while t in s:
        pos = s.find(t)
        s = s[: pos] + s[pos + 1 + len(t):]
        cnt += 1
    print(cnt)
