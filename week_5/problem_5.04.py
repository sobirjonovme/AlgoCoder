"""
https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index1, index2, result_index = 0, 0, 0
        result_array = [int] * (m+n)

        while index1 < m and index2 < n:
            if nums1[index1] > nums2[index2]:
                result_array[result_index] = nums2[index2]
                index2 += 1
                result_index += 1
                continue
            result_array[result_index] = nums1[index1]
            index1 += 1
            result_index += 1
        
        while index1 < m:
            result_array[result_index] = nums1[index1]
            index1 += 1
            result_index += 1
        
        while index2 < n:
            result_array[result_index] = nums2[index2]
            index2 += 1
            result_index += 1
        
        for i in range(m+n):
            nums1[i] = result_array[i]            


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    # # example 2
    # nums1 = [1]
    # m = 1
    # nums2 = []
    # n = 0

    # # example 3
    # nums1 = [0]
    # m = 0
    # nums2 = [1]
    # n = 1
    
    sol.merge(nums1, m, nums2, n)
    print(f"Result:   {nums1}")
