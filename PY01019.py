# import math
nOT = int(input())
for ii in range(nOT):
    s1 = str(input())
    s2 = s1[::-1]
    # print(s1 , s2)
    state = True

    for i in range(len(s1) - 1):
        if abs(ord(s1[i]) - ord(s1[i + 1])) != abs(ord(s2[i]) - ord(s2[i + 1])):
            state = False
            break
    if state:
        print("YES")
    else:
        print("NO")
