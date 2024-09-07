input_list = list(map(int, input().split()))

k = input_list[0]
w = input_list[1]
n = input_list[2]

need_money = 0
for i in range(1, n+1):
    need_money = need_money + (i*k)


if w > need_money:
    print(0)
else:
    print(need_money-w)

 