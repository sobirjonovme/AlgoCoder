"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""

from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        dict_1 = Counter(nums1)
        result = []

        for i in nums2:
            if dict_1[i] > 0:
                result.append(i)
                dict_1[i] -= 1
        
        return result


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    # # example 2
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]

    print(f"Result:   {sol.intersect(nums1, nums2)}")
