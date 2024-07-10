nOT = int(input())

for i in range(nOT):
    n = int(input())
    s = '1'
    j = 2

    # cnt = 0
    while n >= j * j:
        cnt = 0
        while n % j == 0:
            cnt += 1
            n //= j
        if cnt > 0:
            s += " * " + str(j) + "^" + str(cnt)
        j += 1
    if n > 1:
        s += " * " + str(n) + "^" + str(1)
    print(s)