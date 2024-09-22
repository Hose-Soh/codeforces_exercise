def search_for_cycle(graph, node, visited, stack):
    visited[node]= True
    stack[node] = True

    for adjacent in graph[node]:
        if not visited[adjacent]:
            if search_for_cycle(graph, adjacent, visited, stack):
                return True
        elif stack[adjacent]:
            return True
    
    stack[node] = False
    return False


def contains_cycle(graph, vertices):
    visited= [False]*(vertices+1)
    stack = [False]*(vertices+1)

    for v in range(1, vertices+1):
        if not visited[v]:
            if search_for_cycle(graph, v, visited, stack):
                return True
    return False


def main():
    total_planes = int(input())
    connection_sequence = list(map(int, input().split()))

    graph = {i: [] for i in range(1, total_planes+1)}
    #print(graph)

    for j in range(1, total_planes+1):
        if connection_sequence[j-1] != j:
            graph[j].append(connection_sequence[j-1])

    #print(graph)

    output = contains_cycle(graph, total_planes)
    if output:
        print("YES")
    else:
        print("NO")

main()
