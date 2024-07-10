n, k = map(int, input().split())
ar = [int(x) for x in input().split()]

m, fmax, ans, smax = {}, 0, 0, 0
for i in ar :
    if i in m : m[i] += 1
    else : m[i] = 1
    fmax = max(fmax, m[i])
# print(m)
# print(fmax)
for i in range(1, k + 1) :
    if i in m and m[i] > smax and m[i] != fmax :
        smax = m[i]
        ans = i
if ans == 0 : print("NONE")
else : print(ans)
