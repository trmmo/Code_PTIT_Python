n = input()
ls = []
for i in range(len(n) // 2):
    ls.append(n[i * 2: i * 2 + 2])
dc = {}
for s in ls:
    if s in dc:
        dc[s] += 1
    else:
        dc[s] = 1
# ls.sort()
# for _ in ls:
#     print(_, end=" ")
for k, v in dc.items():
    print(k, v)