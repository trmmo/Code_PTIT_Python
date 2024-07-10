ar = str(input()).split(" ")
a = int(ar[0])
k = int(ar[1])
n = int(ar[2])
ls = []

b = k - (a % k)
for i in range(b, n, k):
    if (a + i) % k == 0 and a + i <= n:
        ls.append(str(i))
if len(ls) == 0:
    print(-1)
else:
    s = " ".join(ls)
    print(s)