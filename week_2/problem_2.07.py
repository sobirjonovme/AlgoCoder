# https://leetcode.com/problems/smallest-index-with-equal-value/

def smallestEqual(nums: list[int]) -> int:

    for i in range(len(nums)):
        if i % 10 == nums[i]:
            return i
    
    return -1


nums = [0,1,2]
nums = [4,3,2,1]
nums = [1,2,3,4,5,6,7,8,9,0]

print(smallestEqual(nums))
