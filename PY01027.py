s = input()


def isonly68(s):
    for i in s:
        if i != '6' and i != '8':
            return False
    return True

# print(s.find('688'))


def check(s):
    if isonly68(s):
        if '688' in s:
            for i in range(len(s) // 3):
                if s[i * 3: i * 3 + 3] != '688':
                    return False
            return True
        elif '68' in s:
            for i in range(len(s) // 2):
                if s[i * 2: i * 2 + 2] != '68':
                    return False
            return True
        else:
            for i in range(len(s)):
                if s[i] != '6':
                    return False
            return True
    return False


if check(s):
    print("YES")
else:
    print("NO")
