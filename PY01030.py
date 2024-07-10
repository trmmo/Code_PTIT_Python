ar = str(input()).split(" ")
n = int(ar[0])
k = int(ar[1])
ls = []
# print(n,k)
def gcd(a, b):
    while  b != 0:
        r = a % b
        a = b
        b = r
    return a


for i in range(10 ** (k - 1), 10 ** k):
    if gcd(n, i) == 1:
        ls.append(i)


for i in range(len(ls)):
    if i % 10 != 9:
        print(ls[i], end=" ")
    else:
        print(ls[i])