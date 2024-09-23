user_input = input()
counter = 0
for i in range(len(user_input)):
    if user_input[i] == '7' or user_input[i]== '4':
        counter+=1

# print(counter)
if counter == 4 or counter==7:
    print("YES")
else:
    print("NO")

