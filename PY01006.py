nOT = int(input())

def check(s):
    for i in s:
        if i != '4' and i != '7':
            return False
    return True
for i in range(nOT):
    s = str(input())
    if check(s):
        print("YES")
    else:
        print("NO")