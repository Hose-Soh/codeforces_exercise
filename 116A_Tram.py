t_stops = int(input())
cap_track = 0
cap_list =[]

for i in range(t_stops):
    pass_exit, pass_in = map(int, input().split())
    #print(pass_exit, pass_in)
    if i<t_stops-1:
        cap_track-=pass_exit
        cap_track+=pass_in
        cap_list.append(cap_track)
    #print(capacity)

print(max(cap_list))
