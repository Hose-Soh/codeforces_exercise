step = int(input(""))
result = 0
i=0

while(i<step):
    operation = []
    user_input = input("")
    operation.append(user_input)
    
    if len(operation[0]) <=3 and (operation[0][0]=='X' or operation[0][2] == 'X'):
        if operation[0][0] == '-' or operation[0][2]=='-':
            result -= 1
            
        elif operation[0][0] == '+' or operation[0][2]=='+':
            result+=1
    else:
        continue     

    i+=1

print(result)