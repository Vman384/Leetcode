from typing import List


def jump(nums: List[int]) -> int:
        nums.reverse()
        print(nums)
        jumpDict = {}
        jumpDict[(nums[0],0)] = 0
        index = 1
        while index<len(nums):
            jump = nums[index]
            minJump = float('inf')
            for i in range(index-1,index-jump-1,-1):
                if i < 0:
                    break
                if jumpDict[(nums[i],i)] < minJump:
                     minJump = jumpDict[(nums[i],i)]

            jumpDict[(nums[index],index)] = minJump+1
            index += 1
        return jumpDict[(nums[len(nums)-1],len(nums)-1)]

nums = [2,3,0,1,4]
print(jump(nums))

def jump(nums: List[int]) -> int:
        jumps, max_reach, steps = 0, 0, 0

        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i])
            if i == steps:
                jumps += 1
                steps = max_reach
        return jumps