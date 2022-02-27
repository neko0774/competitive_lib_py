from heapq import heappush, heappop, heapify

def prim(G, s=0, N=0):
  #G = graph, s = start, N is a number of edges
  #G looks like this
  #G = [[(u, cost), (v, cost)], [...], ...]
  if N==0:
    N = len(G)
  seen = [False]*N
  seen[s] = True
  cnt = 0
  ans = 0

  q = []
  heapify(q)
  for i, j in G[0]:
    heappush(q, (i, j))
  
  while cnt<N:
    v, cost = heappop(q)
    if seen[v]: continue
    seen[v] = True
    cnt += 1
    ans += cost
    for i,j in G[v]:
      if seen[i]: continue
      heappush(q, (i, j))
  return ans



V, E = map(int, input().split())
G = [[] for _ in range(V)]
for i in range(E):
  s, t, w = map(int, input().split())
  G[s].append((t, w))
  G[t].append((s, w))
print(prim(G))
