nOT = int(input())


for i in range(nOT):
    n = int(input())
    s = 0.0
    init = 0
    if n % 2 == 0:
        init = 2
    else:
        init = 1
    for j in range(init, n + 1, 2):
        s += 1 / j
    res = "%.6f" % s
    print(res)
