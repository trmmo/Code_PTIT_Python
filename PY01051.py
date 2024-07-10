nOT = int(input())

for i in range(nOT):
    s = str(input())
    t = 0
    for j in range(len(s)):
        t += int(s[j])
    st = str(t)
    if st[::-1] == str(t) and len(st) > 1:
        print("YES")
    else:
        print("NO")
