nOT = int(input())
for i in range(nOT):
    n = int(input())
    j = 0
    while n % 7 != 0 and j <= 1000:
        s = str(n)
        s = s[::-1]
        n += int(s)
        j += 1
    if n % 7 == 0:
        print(n)
    else:
        print(-1)