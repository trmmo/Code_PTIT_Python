n = int(input())
pro = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in range(n):
    n, b = map(int, input().split())
    s = ""
    while n > 0:
        s += pro[n % b]
        n //= b
    s = s[::-1]
    print(s)
#     if b == 2:
#         s = str(bin(n)).upper()
#         print(s[2:])
#     elif b == 8:
#         s = str(oct(n)).upper()
#         print(s[2:])
#     elif b == 16:
#         s = str(hex(n)).upper()
#         print(s[2:])
    # print()
