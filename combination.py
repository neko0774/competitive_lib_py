def combination(x,y):
    ans = 1
    y = min(y, x-y)
    for i in range(1,x-y+1):
        ans *= (x-i+1)
        ans //= i
    return ans