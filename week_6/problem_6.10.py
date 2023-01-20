"""
https://leetcode.com/problems/intersection-of-two-arrays/
"""


class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return [i for i in set1 if i in set2]
        
        return [i for i in set2 if i in set1]


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    # # example 2
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]

    print(f"Result:   {sol.intersection(nums1, nums2)}")
