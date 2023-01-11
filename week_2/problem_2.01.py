# https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array

def countPairs(nums: list[int], k: int) -> int:

    n = len(nums)
    count = 0

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] == nums[j] and (i*j)%k == 0:
                count += 1
    
    return count

nums = [3, 1, 2, 2, 2, 1, 3]
k = 2

print(countPairs(nums, k))

