import math

def min_steps(n, k):
    if k == 1:
        return n  

    step = 0
    while n > 0:
        step += n % k  
        n //= k  
    return step



t = int(input())  

for _ in range(t):
    n, k = map(int, input().split())
    
    print(min_steps(n, k))