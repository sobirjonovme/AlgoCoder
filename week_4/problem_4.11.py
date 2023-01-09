"""
https://leetcode.com/problems/robot-return-to-origin/
"""

# 'R' (right), 
# 'L' (left), 
# 'U' (up), and 
# 'D' (down).

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        position = [0, 0]

        for i in moves:
            if i == 'U':
                position[1] += 1
            elif i == 'D':
                position[1] -= 1
            elif i == 'R':
                position[0] += 1
            elif i == 'L':
                position[0] -= 1

        return position == [0, 0]


if __name__ == '__main__':
    sol = Solution()

    moves = "UD"
    # moves = "LL"

    print(f"Return:   {sol.judgeCircle(moves)}")
