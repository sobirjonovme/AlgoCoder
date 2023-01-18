"""
https://leetcode.com/problems/find-peak-element/
"""


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        
        left = 1
        right = len(nums)-2

        while left <= right:
            midpoint = left + (right-left)//2

            if nums[midpoint-1] < nums[midpoint] and nums[midpoint] > nums[midpoint+1]:
                return midpoint

            if nums[midpoint+1] > nums[midpoint]:
                left = midpoint+1
                continue
            right = midpoint-1 


if __name__ == '__main__':
    sol = Solution()

    nums = [1,2,3,1]
    # nums = [1,2,1,3,5,6,4]

    print(f"Result:   {sol.findPeakElement(nums)}")
