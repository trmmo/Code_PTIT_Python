t = int(input())

for i in range(t):
    s1 = input()
    s2 = input()
    l1 = [char for char in s1]
    l2 = [char for char in s2]
    l1.sort()
    l2.sort()
    print("Test " + str(i + 1) + ": ", end="")
    if l2 == l1:
        print("YES")
    else:
        print("NO")