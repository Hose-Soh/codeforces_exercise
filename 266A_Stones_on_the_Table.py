total_stone = int(input())
stone_clr_combination = list(input().lower())
total_stone_move = 0

for i in range(1, total_stone):
    if stone_clr_combination[i] == stone_clr_combination[i-1]:
        total_stone_move+=1

print(total_stone_move)
