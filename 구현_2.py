# 시각
n = int(input())
cnt = 0
for i in range(0,n+1):
    for j in range(0,60):
        for h in range(0,60):
            num = str(i)+str(j)+str(h)
            if '3' in num:
                cnt +=1

print(cnt)

