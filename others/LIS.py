from bisect import bisect_left as bl
inf = 10**12
def LIS(array):
    dp = [inf for _ in range(len(array))]
    for a in array:
        dp[bl(dp, a)] = a
    return bl(dp, inf)