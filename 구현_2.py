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






# cnt = 0
# for i in n:
#     if i == 3 or i==13 or i==23:
#         cnt += 60 * 60
#     else:
#         for j in range(1,61):
#             if j in [3,13,23,33,43,53]


