friend_coord = int(input())

steps = 0

for i in range(5, 0, -1):
    steps = steps + int(friend_coord/i)

    friend_coord-=int(friend_coord/i)*i

print(steps)
    

