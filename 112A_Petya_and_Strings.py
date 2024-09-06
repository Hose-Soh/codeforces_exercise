string_1 = input().lower()
string_2 = input().lower()
uncommon = []

string_1_score = [ord(i) for i in string_1]
string_2_score = [ord(j) for j in string_2]




if string_1_score > string_2_score:
    result = 1
elif string_1_score < string_2_score:
    result = -1
else:
    result = 0

print(result)