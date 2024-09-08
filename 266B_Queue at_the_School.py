user_input1 = list(map(int, input().split()))
student_number = user_input1[0]
time = user_input1[1]

line_sequence = list(input())

for t in range(time):
    for i in range(student_number-1, 0, -2):
        if line_sequence[i] == 'B' and line_sequence[i+1]=='G':
            line_sequence[i] = 'G'
            line_sequence[i+1] = 'B'

output = "".join(line_sequence)
print(output)