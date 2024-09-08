user_input1 = list(map(int, input().split()))
student_number = user_input1[0]
time = user_input1[1]

line_sequence = list(input())

for t in range(time):
    i = 0
    while i<student_number-1:

        if line_sequence[i] == 'B' and line_sequence[i+1]=='G':
            line_sequence[i] = 'G'
            line_sequence[i+1] = 'B'
            i+=2
        else:
            i+=1

output = "".join(line_sequence)
print(output)