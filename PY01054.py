nOT = int(input())

for i in range(nOT):
    s = str(input())
    t = 1
    for j in range(len(s)):
        if int(s[j]) > 0:
            t *= int(s[j])
    print(t)
