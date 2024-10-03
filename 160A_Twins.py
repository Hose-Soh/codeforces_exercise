n = int(input())

coin_list = sorted(list(map(int, input().split())), reverse=True)
thold_value = sum(coin_list)//2
temp_sum = 0
counter = 0

for i in range(n):
    if temp_sum<=thold_value:
        temp_sum+=coin_list[i]
        counter+=1
    else:
        break

print(counter)