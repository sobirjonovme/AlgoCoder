"""
https://leetcode.com/problems/search-a-2d-matrix/
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        up = 0
        bottom = len(matrix)-1 
        row = -1
        
        while up <= bottom:
            mid = up + (bottom-up)//2

            if matrix[mid][0] == target:
                return True
            
            if matrix[mid][0] < target:
                up = mid + 1
                row = mid
                continue

            bottom = mid - 1
        
        if row == -1:
            return False

        left = 0
        right = len(matrix[row])-1

        while left <= right:
            mid = left + (right-left)//2

            if matrix[row][mid] == target:
                return True
            
            if matrix[row][mid] < target:
                left = mid + 1
                continue
            right = mid - 1
        
        return False


if __name__ == '__main__':
    sol = Solution()

    # example 1
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3

    # #example 2
    # matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    # target = 13

    print(f"Result:   {sol.searchMatrix(matrix, target)}")
