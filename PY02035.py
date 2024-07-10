n = input()
k = int(input())
ls = []
for i in range(len(n) // 2):
    ls.append(n[i * 2: i * 2 + 2])
ls.sort()
dc = {}
for s in ls:
    if s in dc:
        dc[s] += 1
    else:
        dc[s] = 1
# ls.sort()
# for _ in ls:
#     print(_, end=" ")
# dc = sorted(dc, key = lambda dc: dc[0])
bl = False
for key, v in dc.items():
    if dc[key] >= k:
        print(key, v)
        bl = True
if not bl:
    print("NOT FOUND")