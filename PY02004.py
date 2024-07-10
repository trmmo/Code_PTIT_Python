n = int(input())
ar = input().split(" ")
cnt = 0

for i in range(1, n):
    if ar[i] != ar[i - 1]:
        cnt += 1
print(cnt)

# stack = []
# cnt = 0
# used = []
#
# for i in range(n):
#     used.append(False)
#
# for i in range(n - 1):
#     if ar[i] != ar[i + 1] and used[i] == used[i + 1] == False:
#         cnt += 1
#         used[i] = used[i + 1] = True
# print(cnt)