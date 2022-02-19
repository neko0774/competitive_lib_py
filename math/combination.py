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