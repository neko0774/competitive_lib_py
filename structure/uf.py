class UnionFind:
    def __init__(self, N):
        self.root = list(range(N + 1))
        self.size = [1] * (N + 1)
 
    def __getitem__(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x
 
    def merge(self, x, y):
        x = self[x]
        y = self[y]
        if x == y:
            return
        sx, sy = self.size[x], self.size[y]
        if sx < sy:
            x, y = y, x
            sx, sy = sy, sx
        self.root[y] = x
        self.size[x] += sy
    

#書きなれてるほう
def find_root(x):
    if x == root[x]: return x
    root[x] = find_root(root[x])
    return root[x]

def merge(x,y):
    rx,ry = find_root(x),find_root(y)
    root[rx] = ry
