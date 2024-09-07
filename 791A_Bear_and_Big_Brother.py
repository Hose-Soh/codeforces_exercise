input_list = list(map(int, input().split()))

limak = input_list[0]
bob = input_list[1]
year = 0 

while limak <= bob:
    limak *= 3
    bob*=2
    year+=1

print(year)