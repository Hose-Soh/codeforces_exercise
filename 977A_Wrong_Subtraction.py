user_input = list(map(int, input().split()))
number = user_input[0]
steps = user_input[1]

for i in range(steps):
    if (number)%10==0:
        number = int(number/10)
    else:
        number-=1

print(number)