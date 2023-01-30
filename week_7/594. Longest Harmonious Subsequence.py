"""
https://leetcode.com/problems/longest-harmonious-subsequence/
"""

from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        nums_count = Counter(nums)
        result = 0

        for num in nums_count.keys():
            if num+1 in nums_count:
                temp = nums_count[num] + nums_count[num+1]
                if temp > result:
                    result = temp
        
        return result



if __name__ == '__main__':
    sol = Solution()

    nums = [1, 3, 2, 2, 5, 2, 3, 7]
    # nums = [1, 2, 3, 4]
    # nums = [1, 1, 1, 1]

    print(f"Result:   {sol.findLHS(nums)}")
