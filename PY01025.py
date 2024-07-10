s = str(input())


s = s[::-1]
s1 = ''
for i in range(len(s)):
    s1 += s[i]
    if i % 3 == 2 and i != len(s) - 1:
        s1 += ','
s1 = s1[::-1]
print(s1)