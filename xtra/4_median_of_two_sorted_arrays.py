"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        total_length = len(nums1) + len(nums2)
        mid = (total_length+1) // 2

        index1, index2 = 0, 0
        counter = 0

        while counter < (mid-1) and index1 < len(nums1) and index2 < len(nums2):
            counter += 1
            if nums1[index1] < nums2[index2]:
                index1 += 1
                continue
            index2 += 1

        while counter < (mid-1) and index1 < len(nums1):
            counter += 1
            index1 += 1
        
        while counter < (mid-1) and index2 < len(nums2):
            counter += 1
            index2 += 1
        
        if index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                result = nums1[index1]
                index1 += 1
            else:
                result = nums2[index2]
                index2 += 1
        elif index1 < len(nums1):
            result = nums1[index1]
            index1 += 1
        elif index2 < len(nums2):
            result = nums2[index2]
            index2 += 1
        
        if total_length%2 == 1:
            return result
        
        if index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] < nums2[index2]:
                return (result + nums1[index1]) / 2
            return (result + nums2[index2]) / 2
        if index1 < len(nums1):
            return (result + nums1[index1]) / 2
        if index2 < len(nums2):
            return (result + nums2[index2]) / 2


if __name__ == '__main__':
    sol = Solution()

    # example 1
    nums1 = [1, 3]
    nums2 = [2]

    # # example 2
    # nums1 = [1, 2]
    # nums2 = [3, 4]

    # example 3
    nums1 = []
    nums2 = [1, 2, 3, 4]

    # example 4
    nums1 = [4]
    nums2 = [1, 2, 3]

    print(f"Result:   {sol.findMedianSortedArrays(nums1, nums2)}")
