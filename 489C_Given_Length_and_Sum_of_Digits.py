def min_max_sum(m, s):
    if s==0:
        if m==1:
            return 0, 0
        else:
            return -1, -1
        
    if s > 9 * m:
        return -1, -1
    
    mn = []
    mx = []
    rem_sum = s

    # find min
    for i in range(m):
        for d in range(0 if i>0 else 1, 10):
            if rem_sum-d>=0 and rem_sum-d<=9*(m-i-1):
                mn.append(str(d))
                rem_sum-=d
                break
    
    rem_sum = s
    # find max
    for j in range(m):
        for d in range(9, -1, -1):
            if rem_sum-d>=0 and rem_sum-d<=9*(m-j-1):
                mx.append(str(d))
                rem_sum-=d
                break

    return ''.join(mn), ''.join(mx)

m, s = map(int, input().split())

mini, maxm = min_max_sum(m, s)
print(mini, maxm)