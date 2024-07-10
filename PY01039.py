nOT = int(input())

def check(n):
    for j in range (2, len(n)):
        if n[j] != n[j - 2]:
            return False
    return True

for i in range(nOT):
    n = str(input())
    if check(n):
        print("YES")
    else:
        print("NO")