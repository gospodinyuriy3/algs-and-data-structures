def ternarny_search_iter(array, left, right, target) -> int | bool:
    while left < right:
        m1 = left + (right - left) // 3
        m2 = right - (right - left) // 3
        
        if array[m1] == target:
            return m1
        if array[m2] == target:
            return m2
        
        if target < array[m1]:
            right = m1 - 1
        elif target > array[m2]:
            left = m2 + 1
        else:
            left = m1 + 1
            right = m2 - 1
    return False

