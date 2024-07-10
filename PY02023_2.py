class Number:
    def __init__(self, val):
        self.val = val
        self.productDigit = 1
        while val > 0:
            self.productDigit *= val % 10
            val //= 10


def cmp(_a):
    return _a.productDigit, _a.val


for z in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    l = []
    for i in a:
        l.append(Number(i))
    l.sort(key=cmp)
    for i in l:
        print(i.val, end=' ')
    print()
