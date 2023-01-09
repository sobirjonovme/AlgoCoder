# https://leetcode.com/problems/maximum-ascending-subarray-sum/

def maxAscendingSum(nums: list[int]) -> int:

    max_sub_sum = nums[0]
    sub_sum = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            sub_sum += nums[i]
            continue

        if sub_sum > max_sub_sum:
            max_sub_sum = sub_sum

        sub_sum = nums[i]
    
    if sub_sum > max_sub_sum:
        max_sub_sum = sub_sum

    return max_sub_sum

nums = [10, 20, 30, 40, 50]
nums = [10, 20, 30, 5, 10, 50]
nums = [12, 17, 15, 13, 10, 11, 12]

print(maxAscendingSum(nums))
