"""
https://leetcode.com/problems/as-far-from-land-as-possible/
"""
# 0 -> water
# 1 -> land

from collections import deque

class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        
        n = len(grid)
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
        
        if len(q) == n*n:
            return -1

        mrow = [0, -1, 0, 1]
        mcolumn = [-1, 0, 1, 0]

        answer = -1

        while q:
            answer += 1
            size = len(q)

            for _ in range(size):
                x, y = q.popleft()

                for i in range(4):
                    new_x, new_y = x + mrow[i], y + mcolumn[i]

                    if (0<=new_x and new_x<n) and (0<=new_y and new_y<n) and grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = 1
                        q.append((new_x, new_y))
        
        return answer


if __name__ == '__main__':
    sol = Solution()

    grid = [[1,0,1],[0,0,0],[1,0,1]]
    # grid = [[1,0,0],[0,0,0],[0,0,0]]

    print(f"Result:   {sol.maxDistance(grid)}")
