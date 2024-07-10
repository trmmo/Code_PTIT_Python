nOT = int(input())


def check(n):
    for i in range (0, len(n)):
        if n[i] != '0' and n[i] != '1' and n[i] != '2':
            return False
    return True


for i in range(nOT):
    n = str(input())
    if check(n):
        print("YES")
    else:
        print("NO")