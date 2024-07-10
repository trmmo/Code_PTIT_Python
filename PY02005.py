n = int(input())

ar = []
for i in input().split(" "):
    ar.append(int(i))
cnt = 0

# ls.append(int(ar[0]))
# pls = []
#
# for i in range(1, n):
#     for j in range(i):
#         if ls[j] > int(ar[i]) and [ls[j], int(ar[i])] not in pls:
#             pls.append([ls[j], int(ar[i])])
#             cnt += 1
#         ls.append(int(ar[i]))
# print(cnt)
for i in range(n - 1):
    for j in range(i + 1, n):
        if i < j and ar[i] > ar[j]:
            cnt += 1
print(cnt)
