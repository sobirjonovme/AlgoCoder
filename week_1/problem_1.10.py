# https://leetcode.com/problems/max-consecutive-ones/


def findMaxConsecutiveOnes(nums: list[int]) -> int:

    max_length = 0
    length = 0

    for i in nums:
        if i == 0:
            if length > max_length:
                max_length = length
            length = 0
        elif i == 1:
            length += 1
    
    if length > max_length:
        max_length = length
    
    return max_length

nums = [1, 1, 0, 1, 1, 1]
# nums = [1, 0, 1, 1, 0, 1]

print(findMaxConsecutiveOnes(nums))
