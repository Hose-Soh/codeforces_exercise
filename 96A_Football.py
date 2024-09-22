player_string = input()
c = 1

for i in range(len(player_string)-1):
    if player_string[i] == player_string[i+1]:
        c+=1
        if c>=7:
            print("YES")
            break
    else:
        c=1

if c < 7:
    print("NO")
    