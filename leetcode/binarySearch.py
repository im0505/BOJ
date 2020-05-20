
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        print(left, right, pivot)
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


print(search([5], 5))
