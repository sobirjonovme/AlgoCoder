# https://leetcode.com/problems/running-sum-of-1d-array/


def runningSum1(nums: list[int]) -> list[int]:
    n = len(nums)  
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return nums

def runningSum2(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [None]*n

    ans[0] = nums[0]

    for i in range(1, n):
        ans[i] = ans[i-1] + nums[i]
    
    return ans

arr = [1, 2, 3, 4]

print(runningSum2(arr))
