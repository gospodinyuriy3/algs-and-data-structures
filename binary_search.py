def binary_search(array, target) -> int:
    if len(array) == 0:
        return IndexError

    left = 0
    right = len(array) - 1

    
    return binary_search_iterations(array, left, right, target)
    return binary_search_recurse(array, left, right, target) #работает только если элемент 100% есть в массиве

def binary_search_recurse(array, left, right, target) -> int:
    if left > right:
        return None
    
    mid = left + (right - left) // 2

    if array[mid] == target:
        return mid
    
    if array[mid] > target:
        return binary_search_recurse(array, left, array[mid] - 1, target)
    else:
        return binary_search_recurse(array, array[mid] + 1, right, target)


def binary_search_iterations(array, left, right, target) -> int:
    if left > right:
        return None
    
    while left <= right:
        mid = left + (right - left) // 2
    
        if array[mid] == target:
            return mid
        
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return None
