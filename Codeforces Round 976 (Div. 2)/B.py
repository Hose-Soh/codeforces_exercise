import math

def min_b(k):
   
    n = k + int(math.isqrt(k))
    
    while True:
        
        on_b = n - int(math.isqrt(n))
        
        if on_b == k:
            return n
        
        n += 1

t = int(input())
results = []
for _ in range(t):
    k = int(input())
    print(min_b(k))

