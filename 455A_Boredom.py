def max_points(n, seq):
    max_val = max(seq)+1
    count = [0]*(max_val)
    
    for num in seq:
        count[num]+=1
    
    dp = [0]*(max_val)
    dp[1] = count[1]

    for i in range(2, max_val):
        dp[i] = max(dp[i-2]+count[i]*i, dp[i-1])

    return dp[-1]
    

n = int(input())
seq = list(map(int, input().split()))
score = max_points(n, seq)
print(score)

