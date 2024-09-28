t = int(input())  

for _ in range(t):
    n = int(input())  
    arr = list(map(int, input().split()))  
    
    odd_elements = []
    even_elements = []
    
    for i in range(n):
        if i % 2 == 0:
            odd_elements.append(arr[i])  
        else:
            even_elements.append(arr[i])  
    
   
    odd_score = max(odd_elements) + len(odd_elements) if odd_elements else 0
    even_score = max(even_elements) + len(even_elements) if even_elements else 0
    
   
    print(max(odd_score, even_score))
