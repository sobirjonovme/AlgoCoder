"""
https://leetcode.com/problems/number-of-lines-to-write-string/
"""


# a	-> 97	lowercase a

class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        rows_num = 1
        current_row_length = 0

        for i in s:
            letter_length = widths[ord(i)-97]

            if current_row_length + letter_length <= 100:
                current_row_length += letter_length
                continue

            rows_num += 1
            current_row_length = letter_length
        
        return [rows_num, current_row_length]


if __name__ == '__main__':
    sol = Solution()

    widths = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    s = "abcdefghijklmnopqrstuvwxyz"

    # widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    # s = "bbbcccdddaaa"

    print(f"Result:   {sol.numberOfLines(widths, s)}")