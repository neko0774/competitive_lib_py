N, M = map(int, input().split())#number of node, edge
graph = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A-1].append(B-1)
    graph[B-1].append(A-1)

seen = [0]*N

from collections import deque





def bfs(start, node):
    next = deque(graph[start])
    seen = [0]*node
    for i in next:
        if seen[i]: continue
        seen[i] = 1
        for j in graph[i]
    
