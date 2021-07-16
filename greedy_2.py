#page 92 큰 수의 법칙 (내가 푼 답)
n,m,k = map(int,input().split())
num_list = list(map(int, input().split()))

max_num = max(num_list)
max_cnt = num_list.count(max_num)

num_list.remove(max_num)
sec_num = max(num_list)

if max_cnt == 1:
    print(sec_num * (m//k)+max_num*(m-(m//k)))
elif max_cnt >1:
    print(max_num*m)



