nOT = int(input())

def check(s):
    for i in range(len(s) - 1):
        if (s[i] > s[i + 1]):
            return False
    return True

for i in range(nOT):
    s = str(input())
    if check(s):
        print("YES")
    else:
        print("NO")