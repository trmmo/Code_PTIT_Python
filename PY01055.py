nOT = int(input())


def check(s):
    if len(s) % 2 == 0:
        return False
    if s[0] == s[1]:
        return False
    for i in range(1, len(s)):
        if i % 2 == 0 and s[i] != s[0]:
            return False
    return True

for i in range(nOT):
    s = str(input())
    if check(s):
        print("YES")
    else:
        print("NO")
