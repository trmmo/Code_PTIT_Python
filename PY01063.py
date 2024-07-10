nOT = int(input())

for i in range(nOT):
    x = input()
    y = input()
    j = 0
    cnt = 0
    while j + len(y) - 1 < len(x):
        if x[j:j+len(y)] == y:
            cnt += 1
            j += len(y)
        else:
            j += 1
    print(cnt)
