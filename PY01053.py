nOT = int(input())

for i in range(nOT):
    s = str(input())
    while (len(s) > 1):
        t = 0
        for j in range(len(s)):
            t += int(s[j])
        s = str(t)
    if int(s) % 3 == 0:
        print("YES")
    else:
        print("NO")
