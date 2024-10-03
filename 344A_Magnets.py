n_input = int(input())
magnet_list = []
counter = 1


for i in range(n_input):
    magnet_list.append(input())
    if i>0:
        if magnet_list[i] != magnet_list[i-1]:
            counter+=1

print(counter)