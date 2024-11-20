def maxArea(height: list[int]) -> int:
    maxArea = 0
    left = 0
    right = len(height) -1
    while right>left:
        area = min(height[left],height[right]) * (right - left)
        if area > maxArea:
            maxArea = area
        if height[left] > height[right]:
            right-=1
        else:
            left+=1
    return maxArea


print(maxArea([1,8,6,2,5,4,8,3,7]))