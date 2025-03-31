from binary_search import binary_search_iterations

def exp_search(array, left, right, target) -> int | bool:
    border = 1
    while array[border] < target:
        border *= 2
        if border >= right:
            border = right
            break
    
    return binary_search_iterations(array, border//2, border, target)
