class UnionFind:
	def __init__(self, N):
    self.root = list(range(N + 1))
    self.size = [1] * (N + 1)
 
  def find_root(self, x):
    root = self.root
    while root[x] != x:
      root[x] = root[root[x]]
      x = root[x]
    return x
 
  def merge(self, x, y):
    root, size = self.root, self.size
    x = self.find_root(x)
    y = self.find_root(y)
    if x == y:
  	  return
    if size[x] < size[y]:
      x, y = y, x
    root[y] = root[x]
    size[x] += size[y]
    
  def same(self, x, y):
    return self.find_root(x)==self.find_root(y)
    

#omome
def find_root(x):
  if x == root[x]: return x
  root[x] = find_root(root[x])
  return root[x]

def merge(x,y):
  rx,ry = find_root(x),find_root(y)
  root[rx] = ry
