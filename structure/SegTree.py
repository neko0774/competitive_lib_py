inf = 10**18

class SegTree:
  def __init__(self, N, array=None):
    self.size = 1
    while self.size < N:
      self.size *= 2
    self.n = self.size*2-1
    self.tree = [inf]*(self.n)
    if array!=None:
      for i in range(n):
        self.tree[n+i] = array[i]
      for i in range(n-1,0,-1):
        self.tree[i] = compare(self.tree[2*i+1], self.tree[2*i+2])

  def update(self, i, v):
    #0 index
    # update ith value to v
    i += self.size-1
    self.tree[i] = v
    while i>0:
      i = (i-1)//2
      self.tree[i] = self.compare(self.tree[2*i+1], self.tree[2*i+2]) 
  
  def query(self, l, r, k=0, ll=0, rr=None):
    #return the value of the "compare" in [l, r)
    if rr==None:
      rr=self.size
    if rr<=l or r<=ll: return inf
    if l<=ll and rr<=r: return self.tree[k]
    else:
      left = self.query(l, r, 2*k+1, ll, (ll+rr)//2)
      right = self.query(l, r, 2*k+2, (ll+rr)//2, rr)
      return self.compare(left, right) 

  def compare(self, a, b):
    #the condition to return
    #such as min, max, gcd, etc
    return 
    

