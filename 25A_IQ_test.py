n = int(input())

seq = list(map(int, input().split()))

temp_list = [seq[i]%2 for i in range(len(seq))]

if sum(temp_list) == 1:
    ind = temp_list.index(1)
else:
    ind = temp_list.index(0)


#print(temp_list)
print(ind+1)