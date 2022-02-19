class BIT:
  def __init__(self, N):
    self.size = N
    self.data = [0]*(N+1)
  

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
      