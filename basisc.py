def binary_search(sorted_array, index):#二分探索
    left, right = 0, len(sorted_array)+1
    while right > left+1:
        mid = (right+left)//2
        if sorted_array[mid] < index:
            left = mid
        elif sorted_array[mid] > index:
            right = mid
        else:
            return mid
    return mid