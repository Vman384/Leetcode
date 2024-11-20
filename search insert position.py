def searchInsert( nums, target):
    high = len(nums) -1
    low = 0
    while low<=high:
        mid = (high + low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]<target:
            low = mid +1
        else:
            high = mid -1
    return high+1
            

print(searchInsert([1,3,5,6],0))