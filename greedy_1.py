# page 87 거스름돈
money = int(input())

list = [500,100,50,10]
cnt = 0

for i in list:
    cnt += money//i
    money = money%i

print(cnt)