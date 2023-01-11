# https://leetcode.com/problems/smallest-range-i/

def smallestRangeI(nums: list[int], k: int) -> int:
    min_element = nums[0]
    max_element = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < min_element:
            min_element = nums[i]
        if nums[i] > max_element:
            max_element = nums[i]
    
    if max_element-min_element < 2*k:
        return 0
    
    return (max_element-min_element) - 2*k


nums = [0, 10]
k = 2

nums = [1, 3, 6]
k = 3

print(smallestRangeI(nums, k))
