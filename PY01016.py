nOT = int(input())

for i in range(nOT):
    s = str(input())
    res = ""
    for j in range(len(s) // 2):
        cnt = int(s[j * 2 + 1])
        for k in range(cnt):
            res += s[j * 2]
    print(res)