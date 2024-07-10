ls = []

while len(ls) < 10:
    ls += list(map(int, input().split()))

ls2 = []
for i in ls:
    if (i % 42) not in ls2:
        ls2.append(i % 42)
print(len(ls2))