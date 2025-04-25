def get_center_value_index(arr):
    if len(arr) % 2 == 0:
        num_center = arr[len(arr)/2 - 1]
        index_center = len(arr)/2

    num_center = arr[len(arr)//2]
    index_center = len(arr)/2


def correct_binary_search_my_own_attempt(arr,n):
    """
    1) find center (take lower bound)
    2) if n is number, return index
    2) if n > center, search right (check for out of bounds)
    3) else search left
    4) once number found return
    
    """

    for index, num in enumerate(arr):
        num_center = arr[len(arr)//2]
        print('center_num', num_center)
        index_center = len(arr)//2
        print('index_center', index_center)

        if n == num_center:
            print('true')
            index += index_center
            return index
        if n > num_center:
            index += index_center
            new_arr = arr[index_center: len(arr)]
            correct_binary_search_my_own_attempt(new_arr,n)
        else:
            new_arr = arr[index: index_center+1]
            correct_binary_search_my_own_attempt(new_arr,n)
            

def binary_search(arr, n):
    """
    let low, high be 0 and len(arr)... n must always be in the range
    loop:
        {n must always be in [low, high)}
        if low > high:
            break
        middle = low + high / 2
        if n == middle: return middle
        if n > middle:
            shift to right
        else:
            shift to left
    
    """
    low, high = 0, len(arr)
    
    while low < high:
        mid = (low + high) // 2
        x = arr[mid]
        if n == x:
            return mid
        if n > x:
            low = mid + 1
        else:
            high = mid
    
    return None


if __name__ ==  "__main__":
    a = (0,1,3,4)
    b = (-5,-2,0)
    cases = (
        # even size
        (a,0,0),
        (a,1,1),
        (a,4,3),
        # odd size
        (b, -5, 0),
        (b, 0, 2),
        # fail
        (a,2,None),
    )
    for nums, n, exp in cases:
        assert binary_search(nums, n) == exp
    print('ok')
   