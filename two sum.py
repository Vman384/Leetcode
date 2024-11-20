def main(nums,target):
    hist = {}
    for i, n in enumerate(nums):
        if target - n in hist:
            return [hist[target - n], i]
        hist[n] = i
nums = [0,4,3,0]
target = 7
print(main(nums,target))