s = input()


def digitsum(_n):
    _s = 0
    st = str(_n)
    for i in range(len(st)):
        _s += ord(st[i]) - ord('0')
    return _s


if len(s) == 1:
    print(1)
else:
    cnt = 0
    while len(s) > 1:
        n = digitsum(s)
        s = str(n)
        cnt += 1
    print(cnt)
