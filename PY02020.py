n = int(input())
a = list(map(float, input().split()))
Max = max(a)
Min = min(a)
s = 0
cmax = 0
cmin = 0
for i in a:
    s += i
    if i == Max:
        cmax += 1
    if i == Min:
        cmin += 1
print("%.2f" % ((s - cmax * Max - cmin * Min) / (n - cmax - cmin)))
