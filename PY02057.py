n, m = map(int, input().split())
ar = []


def ispalind(n):
    return n == int(str(n)[::-1]) and n > 9


_min_ = 10001
_max_ = 0

for _ in range(n):
    tmp = list(map(int, input().split()))
    _min_ = min(_min_, min(tmp))
    _max_ = max(_max_, max(tmp))
    ar.append(tmp)
bl = False
ls = []
for _ in range(n):
    for __ in range(m):
        if ar[_][__] == _max_ - _min_:
            bl = True
            ls.append(f"Vi tri [{_}][{__}]")
print(_max_ - _min_)
if not bl:
    print("NOT FOUND")
else:
    print(_max_)
    for _ in ls:
        print(_)
