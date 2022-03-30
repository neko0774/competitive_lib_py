
#import sys
#sys.setrecursionlimit(10**6)
def scc(G, rG):
	def dfs(x):
		seen[x] = True
		for nx in G[x]:
			if not seen[nx]:dfs(nx)
		vis.append(x)
	def rdfs(x):
		groups.append(x)
		seen[x] = True
		for nx in rG[x]:
			if not seen[nx]:
				rdfs(nx)
	seen = [False]*len(G)
	vis = []
	for i in range(len(G)):
		if not seen[i]: dfs(i)
	seen = [False]*len(G)
	cycles = []
	for i in vis[::-1]:
		if not seen[i]:
			groups = []
			rdfs(i)
			cycles.append(groups)
	return cycles
