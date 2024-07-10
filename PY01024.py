nOT = int(input())


def check(n):
    ssum = 0
    for j in range(len(n) - 1):
        # sum += abs(ord(n[j]) - ord('0'))
        if abs(ord(n[j]) - ord(n[j+1])) != 2:
            return -1
    for j in range(len(n)):
        ssum += abs(ord(n[j]) - ord('0'))
    if ssum % 10 != 0:
        return -1
    return ssum


for i in range(nOT):
    n = str(input())
    # print(check(n))
    if check(n) != -1:
        print("YES")
    else:
        print("NO")
