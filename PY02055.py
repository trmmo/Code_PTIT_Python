import math

n, m = map(int, input().split())
ar = []


def isprime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


for _ in range(n):
    ar.append(list(map(int, input().split())))
bl = False
_max_ = 0
ls = []
for _ in range(n):
    for __ in range(m):
        if isprime(ar[_][__]):
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
