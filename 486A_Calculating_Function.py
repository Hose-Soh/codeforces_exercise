n = int(input())

total = sum([((-1)**i)*i for i in range(1, n+1)])

print(total)