n, k = map(int, input().split())
odd_count = (n+1)//2


if k>odd_count:
    ans = (k-odd_count)*2
else:
    ans = (2*k)-1

print(ans)