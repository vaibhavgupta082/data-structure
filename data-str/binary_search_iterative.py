def binarySearch(nums , target):
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
    return -1

nums = [-1,2,5,44,65]
print(binarySearch(nums,123))