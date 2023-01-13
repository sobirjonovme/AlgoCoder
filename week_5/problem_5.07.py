"""
https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                if i == k:
                    k += 1
                    continue
                nums[k] = nums[i]
                k += 1

        return k
                


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums = [3, 2, 2, 3]
    val = 3

    # # example 2
    # nums = [0, 1, 2, 2, 3, 0, 4, 2]
    # val = 2

    print(f"Result:   {sol.removeElement(nums, val)}")
