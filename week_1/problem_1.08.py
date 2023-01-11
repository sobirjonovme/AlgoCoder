# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/


def countKDifference(nums: list[int], k: int) -> int:
    result = 0
    n = len(nums)

    for i in range(n):
        for j in range(i, n):
            if abs(nums[i]-nums[j]) == k:
                result += 1

    return result

nums = [3, 2, 1, 5, 4]
k = 2

print(countKDifference(nums, k))
