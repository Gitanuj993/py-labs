nums = [1,2,3,4,5]
target = 1

def binary_search(low, high):

    print("low :", low)
    print("high :", high)

    if low > high:
        return -1

    mid = (low + high) // 2

    if nums[mid] == target:
        return mid

    elif nums[mid] > target:
        return binary_search(low, mid - 1)

    else:
        return binary_search(mid + 1, high)

res = binary_search(0, len(nums) - 1)

print("res is :", res)
