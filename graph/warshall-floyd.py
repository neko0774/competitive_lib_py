inf=10**18
def warshall_floyd(G,N):
    #diifferent type of input format; G
    if N==None: N=len(G)
    dist = [[inf]*N for _ in range(N)]
    for f,to,c in G:
        dist[f][to] = c
    for i in range(N):
        dist[i][i] = 0
    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist
