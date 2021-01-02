from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [
    [],
    [2,3,8],    #1
    [1, 7],     #2
    [1,4,5],
    [3,5],
    [3,4],
    [7],        #4
    [2,6,8],    #3
    [1,7]
]

visited = [False] * 9

bfs(graph, 1 , visited)