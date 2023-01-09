# https://leetcode.com/problems/third-maximum-number/


def thirdMax(nums: list[int]) -> int:

    n = len(nums)

    if n < 3:
        return max(nums)
    
    max1 = nums[0]
    max2 = -2**31-1
    max3 = -2**31-1

    for i in range(1, n):
        if nums[i] >= max1:
            if nums[i] != max1:
                max3 = max2
                max2 = max1
                max1 = nums[i]
        elif nums[i] >= max2:
            if nums[i] != max2:
                max3 = max2
                max2 = nums[i]
        elif nums[i] >= max3:
            max3 = nums[i]
   
    if max3 == -2**31-1:
        return max1

    return max3

nums = [3, 2, 1]
nums = [1, 2]
nums = [2, 2, 3, 1]
nums = [1, 2, 2, 5, 3, 5]

print(thirdMax(nums))      
