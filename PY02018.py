n = int(input())

ar = list(map(int, input().split()))
ar.sort()
for i in ar:
    if i + 1 not in ar:
        print(i + 1)
        break
