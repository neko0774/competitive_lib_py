def warshall_floyd(cost, N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])
                return cost