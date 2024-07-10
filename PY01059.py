nOT = int(input())


def execute(s):
    tong = 0
    tich = 1
    bl = True
    for i in range(len(s)):
        if i % 2 == 0:
            tong += int(s[i])
        elif int(s[i]) != 0:
            tich *= int(s[i])
            bl = False
    if bl == True:
        tich = 0
    print(tong, tich)


for i in range(nOT):
    s = str(input())
    execute(s)

