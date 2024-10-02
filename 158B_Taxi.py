from collections import Counter

def find_min_taxi(n, m_list):
    g_count = Counter(m_list)
    #print(g_count)

    min_taxi = g_count[4]

    
    pair1_3 = min(g_count[1], g_count[3])
    min_taxi = min_taxi + g_count[3]
    g_count[1]-=pair1_3

    min_taxi = min_taxi + g_count[2]//2
    if g_count[2]%2:
        min_taxi+=1
        g_count[1] = max(0, g_count[1]-2)

    min_taxi = min_taxi + g_count[1]//4
    if g_count[1]%4:
        min_taxi+=1

    return min_taxi
            

groups = int(input())
members_list = list(map(int, input().split()))

min_t = find_min_taxi(groups, members_list)
print(min_t)