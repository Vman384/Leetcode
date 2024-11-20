def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i = 0
    j = 0
    nums = []
    while i<m and j<n:
        if nums1[i] < nums2[j]:
            nums.append(nums1[i])
            i+=1
        elif nums1[i] > nums2[j]:
            nums.append(nums2[j])
            j+=1
        else:
            nums.append(nums1[i])
            nums.append(nums2[j])
            i+=1
            j+=1
    while j<n:
        nums.append(nums2[j])
        j+=1
    while i<m:
        nums.append(nums1[i])
        i+=1

    nums1 = nums
    return nums1

print(merge([1,2,3,0,0,0],3,[2,5,6],3))