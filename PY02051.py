___ = int(input())

_a = []
res = []
for _ in range(___):
    _a.append(list(map(int, input().split())))
_sum = 0
for _ in range(___):
    for __ in range(___):
        if _ < __:
            _sum += _a[_][__]
_sum //= (___ - 1)
res = [0 for _ in range(___)]
if ___ == 2:
    res[0] = 1
    res[1] = _sum - res[0]
else:
    __sum = sum(_a[0][1:])
    res[0] = (__sum - _sum) // (___ - 2)
    for _ in range(1, ___):
        res[_] = _a[0][_] - res[0]
for _ in res:
    print(_, end=" ")
"""
4
0 3 6 7
3 0 5 6
6 5 0 9
7 6 9 0
"""
