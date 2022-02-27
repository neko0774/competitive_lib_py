#is_prime l9
#factorization l21
#sort_divisions l36
#commmon_division l46
#combination_with_mod l58
#combination l49


def is_prime(number) -> int:
    if number < 2: return 0
    if number==2: return 1
    if number%2==0: return 0
    i = 3
    while i*i <= number:
        if number%i==0:
            return 0
        i+=2
    return 1


def factorization(x):
    i = 2
    ans = []
    while i**2 <= x:
        e = 0
        while x%i == 0:
            e += 1
            x //= i
        if e>0:
            ans.append([i, e])
        i += 1
    if x!=1: ans.append([x, 1])
    return ans


def sort_divisions(number):#約数列挙
    i = 2
    front, back = [],[number]
    while i*i <= number:
        if number%i==0:
            front.append(i)
            if i!=number//i: back.append(number//i)
        i+=1
    return front+back[::-1]

def common_divisinors(x, y):
    return set(sort_divisions(x))&set(sort_divisions(y))

def comb(x,y):
  ans = 1
  y = min(y, x-y)
  for i in range(1,x-y+1):
    ans *= (x-i+1)
    ans //= i
  return ans


def comb(n, k):#with mod
	a = 1
  b = 1
  for i in range(k):
    a = a*(n-i)%mod
    b = b*(i+1)%mod
  return a * pow(b, mod-2, mod)%mod