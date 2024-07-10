t = int(input())
for i in range(t):
    n = int(input())
    ar = list(map(int, input().split()))

    d = {}
    for j in ar:
        if j not in d.keys():
            d[j] = 1
        else:
            d[j] +=1
    # print(d)
    Max = 0
    val = -1
    for k, v in d.items():
        if d[k] > Max:
            Max = d[k]
            val = k
    # print(val)
    if d[val] > n / 2:
        print(val)
    else:
        print("NO")