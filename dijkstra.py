from heapq import heappush, heappop
inf = 10**9

def dijkstra(s, node):#s = start, n = number of the node
    cost = [inf]*node
    hq = [(0, s)]
    check = [False]*node
    cost[s] = 0
    while hq:
        v = heappop(hq)[1]
        check[v] = True
        for to, weight in e[v]:
            if (not check[to]) and cost[v] + weight < cost[to]:
                cost[to] = cost[v] + weight
                heappush(hq, (cost[to], to))
    return cost

# ノード数, エッジ数, 始点ノード
v, e, r = map(int, input().split())
# adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
e = [[] for _ in range(v)]
for i in range(e):
    s, t, d = map(int, input().split())
    e[s].append((t, d))
    e[t].append((s, d))