"""
https://leetcode.com/problems/maximum-score-after-splitting-a-string/
"""


class Solution:
    def maxScore(self, s: str) -> int:
        left_sum = 0
        right_sum = 0
        result_sum = -1

        for i in s:
            if i == '1':
                right_sum += 1
        
        for i in range(len(s)-1):
            if s[i] == '0':
                left_sum += 1
            elif s[i] == '1':
                right_sum -= 1
            
            if left_sum + right_sum > result_sum:
                result_sum = left_sum + right_sum

        return result_sum


if __name__ == '__main__':
    sol = Solution()

    s = "011101"
    # s = "00111"
    # s = "1111"

    print(f"Result:   {sol.maxScore(s)}")
