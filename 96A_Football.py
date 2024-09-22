player_string = input()
counter = 0

for i in range(len(player_string)-1):
    # if player_string[i] == player_string[i+1]:
    #     counter+=1
    # else:
    #     counter=0
    print(player_string[i], player_string[i+1])

print(counter)
if counter==7:
    print("YES")
    
else:
    print("NO")
    