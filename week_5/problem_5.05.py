"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        
        return k


if __name__ == '__main__':
    sol = Solution()

    # nums = [1,1,2]
    nums = [0,0,1,1,1,2,2,3,3,4]

    print(f"Result:   {sol.removeDuplicates(nums)}")
    print(nums)
