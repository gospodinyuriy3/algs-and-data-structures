def binary_search(array, target) -> int | IndexError:
    if len(array) == 0:
        return IndexError

    left = 0
    right = len(array) - 1

    res = binary_search_iterations(array, left, right, target)

    return IndexError if not(res) else res
    # return binary_search_recurse(array, left, right, target) работает только если элемент 100% есть в массиве

def binary_search_recurse(array, left, right, target) -> int | bool:
    if left > right:
        return False
    
    mid = left + (right - left) // 2

    if array[mid] == target:
        return mid
    
    if array[mid] > target:
        return binary_search_recurse(array, left, array[mid] - 1, target)
    else:
        return binary_search_recurse(array, array[mid] + 1, right, target)


def binary_search_iterations(array, left, right, target) -> int | bool:
    if left > right:
        return False
    
    while left <= right:
        mid = left + (right - left) // 2
    
        if array[mid] == target:
            return mid
        
        if array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False

def left_binary_search(array, left, right, target) -> int | bool:
    while left + 1 < right:
        mid = (right - left) // 2 + left

        if target > array[mid]:
            left = mid
        else:
            right = mid

    if array[left] == target:
        return left
    if array[right] == target:
        return right
    
    return False

def right_binary_search(array, left, right, target) -> int | bool:
    while left + 1 < right:
        mid = (right - left) // 2 + left

        if target < array[mid]:
            right = mid
        else:
            left = mid

    if array[right] == target:
        return right
    if array[left] == target:
        return left
    
    return False
