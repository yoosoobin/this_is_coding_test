# 왕실의 나이트
p = str(input())
r,c = int(p[1]),ord(p[0])-96

cnt = 0

for i in [2,-2]:
    for j in [1,-1]:
        c += i
        r += j
        if 0 < r < 9 and 0 < c < 9:
            cnt += 1
            c -= i
            r -= j
        else:
            c -= i
            r -= j

for i in [2,-2]:
    for j in [1,-1]:
        r += i
        c += j
        if 0 < r < 9 and 0 < c < 9:
            cnt += 1
            r -= i
            c -= j
        else:
            r -= i
            c -= j


print(cnt)