# https://leetcode.com/problems/build-array-from-permutation/


def buildArray(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [int]*n

    for i in range(n):
        ans[i] = nums[nums[i]]
    
    return ans

nums = [0,2,1,5,3,4]

print(buildArray(nums))
