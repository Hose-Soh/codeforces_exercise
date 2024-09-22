test_case = int(input())
vowel_list = ['a', 'e', 'i', 'o', 'u']



for t in range(test_case):
    output = []
    string_len = int(input())
    for v in range(string_len):
        output.append(vowel_list[v%5])
        
        
    string_output = "".join(sorted(output))
    print(string_output)

