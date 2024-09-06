matrix = []
location = []

for i in range(5):
    row = list(map(int, input().split()))

    if len(row)!=5:
        break
    
    if 1 in row:
        location.append(i)
        location.append(row.index(1))

    matrix.append(row)

i_move = abs((location[0]+1)-3)
j_move = abs((location[1]+1)-3)
total_move = i_move + j_move
print(total_move)


        