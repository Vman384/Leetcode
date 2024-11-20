def main(nums):
    for i in range(0,5):
        for i in nums:
            x=0
            for j in nums:
                if i==j:
                    x+=1
                    if x>=2:
                        nums.remove(j)
    return nums
print(main([0,0,0,0,0,0]))
'''
def second(nums):
    nums=set(nums)
    sorted(nums)
    nums=list(nums)
    return nums
print(second([1,1,2]))
'''