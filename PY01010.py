nOT = int(input())
for i in range(nOT):
    s = str(input())
    if s[:2] == s[-2:]:
        print("YES")
    else:
        print("NO")