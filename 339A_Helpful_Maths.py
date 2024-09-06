user_input = list(input())
numerical_list = []

for i in range(0, len(user_input), 2):
     numerical_list.append(user_input[i])
    
order_list = sorted(numerical_list)

#print(order_list)

output=[]
for i in range(len(order_list)):
     output.append(order_list[i])
     if i < (len(order_list)-1):
        output.append('+')

order_list_with_sign = "".join(output)

print(order_list_with_sign)


