while True:
    t = int(input())
    if t == 0:
        break
    ar = []
    for _ in range(t):
        ar.append(int(input()))
    ar.sort()
    if ar[0] == ar[-1]:
        print("BANG NHAU")
    else:
        print(ar[0], ar[-1])
