#page 99 [1이 될 때까지]  (내가 푼 답)
n,k = map(int,input().split())

cnt = 0
while True:
    if n%k ==0:
        n /= k
        cnt += 1
    else:
        n -= 1
        cnt +=1
    if n==1:
        break
print(cnt)