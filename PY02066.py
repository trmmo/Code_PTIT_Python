n = int(input())
ar = [int(x) for x in input().split()]
while len(ar) < n:
    ar.extend(list(map(int, input().split())))
bl = True
for i in range(1, max(ar)):
    if i not in ar:
        bl = False
        print(i)
if bl:
    print("Excellent!")
