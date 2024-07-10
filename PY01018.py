P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."  # _95    .48     Z90

while True:
    n = str(input())
    if n[0] == '0':
        break
    ar = n.split(" ")
    a = int(ar[0])
    b = ar[1]
    res = ""
    for i in b:
        res += P[(P.find(i) + a) % 28]
    res = res[::-1]
    print(res)