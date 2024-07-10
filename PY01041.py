nOT = int(input())


def check(n):
    pos = -1
    for i in range(0, len(n) - 1):
        if n[i] == n[i + 1]:
            return False
        if ord(n[i]) > ord(n[i + 1]):
            pos = i
            break
    if pos == 0 or pos == -1:
        return False
    for i in range(pos, len(n) - 1):
        if ord(n[i]) < ord(n[i + 1]):
            return False
    return True


for i in range(nOT):
    n = str(input())
    if check(n):
        print("YES")
    else:
        print("NO")
