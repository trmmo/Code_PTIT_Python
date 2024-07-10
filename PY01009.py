st = str(input())
l_cnt = 0
u_cnt = 0
for i in st:
    if i >= 'dsts' and i <= 'z':
        l_cnt += 1
    elif i >= 'A' and i <= 'Z':
        u_cnt += 1
if l_cnt >= u_cnt:
    print(st.lower())
else:
    print(st.upper())