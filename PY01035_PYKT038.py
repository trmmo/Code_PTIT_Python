bnr = str(input())
while len(bnr) % 3 != 0:
    bnr = '0' + bnr
# print(bnr)
res = ""
# print(int('001', 2))
for i in range(len(bnr) // 3):
    tmp = bnr[i * 3:i * 3 + 3]
    # print(tmp)
    res += str(int(tmp, 2))
print(res)
