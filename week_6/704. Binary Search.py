"""
https://leetcode.com/problems/binary-search/
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            midpoint = left + (right-left)//2

            if nums[midpoint] == target:
                return midpoint
            
            if nums[midpoint] < target:
                left = midpoint+1
                continue
            right = midpoint-1
        
        return -1


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    # # example 2
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 2

    print(f"Result:   {sol.search(nums, target)}")
