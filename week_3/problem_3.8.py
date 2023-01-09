"""
https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
"""


class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        col_1 = ord(s[0])
        row_1 = int(s[1])

        col_2 = ord(s[3])
        row_2 = int(s[4])

        result = [str]*((col_2-col_1+1)*(row_2-row_1+1))
        index = 0

        for i in range(col_1, col_2+1):
            col = chr(i)
            for j in range(row_1, row_2+1):
                result[index] = col + str(j)
                index += 1
        
        return result


if __name__ == '__main__':
    sol = Solution()

    # s = "K1:L2"
    s = "A1:F1"

    print(f"Result:   {sol.cellsInRange(s)}")
    