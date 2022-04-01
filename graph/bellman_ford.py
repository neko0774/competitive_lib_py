inf = 10**18
def bellman_ford(r, G, N, M) -> list:
    #r is a starting node
    #D is a graph
    #note the foramt is different
    #N is the number of edges
    #M is the number of vertices
    dist = [inf]*N
    dist[r] = 0
    i=0
    while True:
        if i>N-1: return [0]+dist
        update=False
        for j in range(M):
            f,to,c = G[j]
            if dist[f]!=inf and dist[to]>dist[f]+c:
                dist[to] = dist[f]+c
                update=True
        if not update: break
        i+=1
    return [1]+dist

N,M,r = map(int, input().split())
G = []
for _ in range(M):
    u,v,c=map(int, input().split()) 
    G.append([u,v,c])
    #G.append([v,u,c])
s = bellman_ford(r,G,N,M)
if not s[0]: print("NEGATIVE CYCLE")
else:
    for i in s[1:]:
        print(i if i!=inf else "INF")

#ref
#https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_B