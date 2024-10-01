def max_pair(n, bs_list, m, gs_list):
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if abs(bs_list[i-1]-gs_list[j-1]) <= 1:
                dp[i][j] = dp[i-1][j-1]+1
            dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])
            
    return dp[n][m]
    

total_boys = int(input())
boys = sorted(list(map(int, input().split())))
total_girls = int(input())
girls = sorted(list(map(int, input().split())))
pairs = max_pair(total_boys, boys, total_girls, girls)
print(pairs)