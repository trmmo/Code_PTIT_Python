l0 = [0, 0, 0, 0]


def check(s):
    for i in range(1, len(s)):
        if s[i] != s[0]:
            return False
    return True


while True:
    ls = list(map(int, input().split()))
    # print(ls)
    if ls == l0:
        break
    cnt = 0
    while not check(ls):
        lt = []
        for i in range(len(ls) - 1):
            lt.append(abs(ls[i] - ls[i + 1]))
        lt.append(abs(ls[3] - ls[0]))
        ls = lt
        cnt += 1
    print(cnt)
