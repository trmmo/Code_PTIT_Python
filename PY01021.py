t = int(input())

for _ in range(t):
    s = input()
    sum = 0
    tmp = []
    for i in range(len(s)):
        if s[i].isdigit():
            sum += int(s[i])
        else:
            tmp.append(s[i])
    tmp.sort()
    for i in tmp:
        print(i, end="")
    print(sum)
