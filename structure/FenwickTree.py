class BIT:
  #1th index
  def __init__(self, N, A=None):
    self.size = N
    self.data = [0]*(N+1)
    if A:
      for i in range(N):
        self.add(i+1, A[i])

  def rsum(self, l, r):
    return self.sum(l)-self.sum(r)

  

  def sum(self, r):
    s = 0
    while r>0:
      s += self.data[r]
      r -= r&-r
    return s
  
  def add(self, i, x):
    while i<=self.size:
      self.data[i] += x
      i += i&-i 
      