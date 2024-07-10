# import math

n, m = map(int, input().split())
ar = []


def ispalind(n):
    return n == int(str(n)[::-1]) and n > 9


for _ in range(n):
    ar.append(list(map(int, input().split())))
bl = False
_max_ = 0
ls = []
for _ in range(n):
    for __ in range(m):
        if ispalind(ar[_][__]):
            bl = True
            if ar[_][__] > _max_:
                _max_ = ar[_][__]
                ls.clear()
                ls.append(f"Vi tri [{_}][{__}]")
            elif ar[_][__] == _max_:
                ls.append(f"Vi tri [{_}][{__}]")
if not bl:
    print("NOT FOUND")
else:
    print(_max_)
    for _ in ls:
        print(_)
