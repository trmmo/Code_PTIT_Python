nOT = int(input())
for i in range(nOT):
    ar = str(input()).split(" ")
    n = float(ar[0])
    x = float(ar[1])
    m = float(ar[2])
    cnt = 0
    while n < m:
        n += n * (x / 100)
        cnt += 1
    print(cnt)