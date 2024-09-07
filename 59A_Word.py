input_string = input()
string_list = list(input_string)

lower = 0
upper = 0
for char in string_list:
    if char.isupper():
        upper+=1
    if char.islower():
        lower+=1

if upper > lower:
    output = input_string.upper()
else:
    output = input_string.lower()

print(output)
