s_1 = list(map(int, input()))
s_2 = list(map(int, input()))

ans = [int(bool(s_1[i])^bool(s_2[i])) for i in range(len(s_1))]
#print(ans)
print("".join(map(str, ans)))