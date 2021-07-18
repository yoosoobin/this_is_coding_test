#왕실의 나이트
pos = input()
row = int(pos[1])
column = int(ord(pos[0])-ord('a')+1)

steps = [(-2,-1),(-2,1),(2,-1),(2,1),(1,2),(-1,2),(1,-2),(-1,-2)]

result = 0

for step in steps:
    next_row = row + step[0]
    next_col = column + step[1]

    if 1<=next_col<=8 and 1<=next_row<=8:
        result +=1

print(result)