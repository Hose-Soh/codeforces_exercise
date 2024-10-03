n = int(input())

p_list = list(map(int, input().split()))

pair_ip = {i: p_list[i-1] for i in range(1, n+1)}
output = [k for k, v in sorted(pair_ip.items(), key = lambda item: item[1])]

print(" ".join(map(str, output)))