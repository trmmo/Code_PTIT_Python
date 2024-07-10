nOT = int(input())

f = [1, 1]
for i in range(2, 92):
    c = f[i-1] + f[i-2]
    f.append(c)

for i in range(nOT):
    ar = str(input()).split(" ")
    a = int(ar[0])
    b = int(ar[1])
    for j in range(a, b + 1):
        print(f[j - 1], end=" ")
    print()
