def compute_max_rib(n, a, b, c):
    dp=[-float('inf')]*(n+1)
    dp[0] = 0

    for i in range(1, n+1):
        if i>=a:
            dp[i] = max(dp[i], dp[i-a]+1)
        if i>=b:
            dp[i] = max(dp[i], dp[i-b]+1)
        if i>=c:
            dp[i] = max(dp[i], dp[i-c]+1)

    return dp[n]


r_len, a, b, c = map(int, input().split())
output = compute_max_rib(r_len, a, b, c)
if output>0:
    print(output)
else:
    print(0)
