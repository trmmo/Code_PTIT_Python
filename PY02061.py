t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    h = []
    for i in range(3):
        h.append(list(map(int, input().split())))
    y = []
    for i in range(n - 2):
        tmp = []
        for j in range(m - 2):
            tmp.append(0)
        y.append(tmp)
    for i in range(n - 2):
        for j in range(m - 2):
            s = 0
            for _i in range(i, i + 3):
                for _j in range(j, j + 3):
                    # y[i][j] = h[i][j] * x[_i][_j]   # + h[-1][0] * x[i + 1][j] + h[-1][1] * x[i + 1][j] + h[0][-1] * x[i][j + 1] + h[0][0] * x[i][j] + h[0][1] * x[i][j - 1] + h[1][-1] * x[i - 1][j + 1] + h[1][0] * x[i - 1][j] + h[1][1] * x[i - 1][j - 1]
                    s += x[_i][_j] * h[_i - i][_j - j]
                    y[i][j] = s
    print(sum([sum(_) for _ in y]))

"""
1
4 4
1 1 2 4
5 6 7 8
3 2 1 0
1 2 3 4
1 1 1
1 8 1
1 1 1
-1 -1 -1
-1 8 -1
-1 -1 -1
"""
