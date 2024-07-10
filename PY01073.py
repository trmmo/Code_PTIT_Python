s = input()
used = [False] * 15


def Try(a):
    if len(a) == len(s):
        print(a)
        return
    for i in range (len(s)):
        if not used[i]:
            used[i] = not used[i]
            Try(a + s[i])
            used[i] = not used[i]

Try("")
