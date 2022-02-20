
from heapq import heappush, heappop
def prim(N, G, s=0):
  #G looks like this
  #G = [[(u, cost), (v, cost)]]
  seen = [False]*N
  seen[s] = True
  cnt = 0
  ans = 0

  q = []
  heapq.heapify(q)
  for i, j in G[0]:
    heapq.heappush(q, (i, j))
  
  while cnt<N:
    v, cost = heapq.heappop(q)
    if seen[v]: continue
    seen[v] = True
    cnt += 1
    ans += cost
    for i,j in graph[v]:
      if seen[i]: continue
      heapq.heappush(q, (i, j))
  return ans
