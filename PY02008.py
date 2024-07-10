import math

ls = []


def init(n):
    X = 0
    i = 2
    flag = False
    while X < n:
        flag = True
        for j in range(2, math.floor(math.sqrt(i)) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            ls.append(i)
            # print(i, end=" ")
            X += 1
        i += 1


n, x = map(int, input().split())
init(n)
print(x, end=" ")
for i in ls:
    x += i
    print(x, end=" ")

