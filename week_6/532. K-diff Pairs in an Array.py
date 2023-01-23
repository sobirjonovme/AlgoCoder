"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""

from collections import Counter


class Solution:
    def findPairs(self, nums: list[int], k: int) -> int:
        nums_dict = Counter(nums)
        counter = 0

        for number in nums_dict:
            # if k = 0
            condition1 = (k == 0) and (nums_dict[number] > 1)
            # if k > 0
            condition2 = (k > 0) and (number+k in nums_dict)

            if condition1 or condition2:
                counter += 1

        return counter        


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums = [3, 1, 4, 1, 5]
    k = 2

    # #example 2
    # nums = [1, 2, 3, 4, 5]
    # k = 1

    # # example 3
    # nums = [1, 3, 1, 5, 4]
    # k = 0

    print(f"Result:   {sol.findPairs(nums, k)}")
    