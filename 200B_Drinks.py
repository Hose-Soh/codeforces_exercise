total_drink = int(input())
fraction_list = list(map(int,input().split()))


sum = 0
for drink_frac in fraction_list:
    sum+=drink_frac

result = float(sum/total_drink)
print(result)