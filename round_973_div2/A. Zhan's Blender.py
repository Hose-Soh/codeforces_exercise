t = int(input())

for _ in range(t):
    n = int(input())
    can_put, total_cap = map(int, input().split())
    blender_done = 0
    in_blender = 0
    time = 0
    

    while blender_done < n:
        while in_blender < total_cap:
            blender_done+=can_put
            time+=1
        
        in_blender = 0

    print(time) 