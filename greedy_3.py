# page 96 숫자 카드 게임 (내가 푼 답)
n,m = map(int, input().split())
card_list = []
min_list = []
for i in range(n):
    card_list.append(list(map(int, input().split())))

for j in range(n):
    min_list.append(min(card_list[j]))

print(max(min_list))