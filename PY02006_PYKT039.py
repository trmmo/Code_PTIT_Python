nOT = int(input())


def check(ls1, ls2):
    ls1.sort()
    ls2.sort()
    for i in range(n):
        if ls1[i] > ls2[i]:
            return False
    return True


for i in range(nOT):
    n = int(input())
    ls1 = list(map(int, input().split()))
    ls2 = list(map(int, input().split()))
    if check(ls1, ls2):
        print("YES")
    else:
        print("NO")
