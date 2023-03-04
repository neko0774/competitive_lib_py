#s_prime l9
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


def sort_divisions(number)->list:#約数列挙
    if number==1: return 1
    i = 2
    front, back = [1],[number]
    while i*i <= number:
        if number%i==0:
            front.append(i)
            if i!=number//i: back.append(number//i)
        i+=1
    return front+back[::-1]

def common_divisinors(x, y):
    return set(sort_divisions(x))&set(sort_divisions(y))

fac = [0]*2*10**5
finv = [0]*2*10**5
inv = [0]*2*10**5
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1
for i in range(2, 2*10**5):
    fac[i] = fac[i-1]*i%mod
    inv[i] = mod-inv[mod%i]*(mod//i)%mod
    finv[i] = finv[i-1]*inv[i]%mod


def inv_mod(x,p=mod):
    return pow(x,p-2,p)

def comb(a, b, p=10**9+7):
    if a<b: return 0
    elif a<0 or b<0: return 0
    return fac[a]*(finv[b]*finv[a-b]%p)%p

def comb(n, k):#with mod
    a = 1
    b = 1
    for i in range(k):
        a = a*(n-i)%mod
        b = b*(i+1)%mod
    return a * pow(b, mod-2, mod)%mod


def osak(x):
    t = [0]*(x+1)
    for n in range(2, x+1):
        if t[n]!=0: continue
        t[n] = 1
        for nn in range(2*n, x+1, n):
            t[nn] = n
    return t
            