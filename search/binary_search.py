def binary_search(sorted_list, index):
    lo = 0
    hi = len(sorted_list)
    while lo < hi:
        mid = (lo+hi)//2
        if index < sorted_list[mid]: hi = mid
        else: lo = mid+1
    return lo


#めぐる式
def bs(array, index):
    lo, hi = -1, len(array)
    while abs(hi-lo)>1:
        mid = (lo+hi)//2
        if is_ok(mid, index): hi = mid
        else: lo = mid
    return hi