n_friends, fence_h = map(int, input().split())
frnd_h = list(map(int, input().split()))
width = 0

for height in frnd_h:
    #print(height)
    if height>fence_h:
        width+=2
    else:
        width+=1
    #print(width)

print(width)