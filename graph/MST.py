
from heapq import heappush, heappop
def prim(N, G, s=0):
  seen = [False]*N
  seen[s] = True
  cnt = 0