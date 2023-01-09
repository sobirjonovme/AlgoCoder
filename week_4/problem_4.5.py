"""
https://leetcode.com/problems/license-key-formatting/
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        reverse_result = ''
        temp = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] != '-':
                if temp == k:
                    reverse_result += '-'
                    temp = 0

                reverse_result += s[i].upper()
                temp += 1

        return reverse_result[::-1]


if __name__ == '__main__':
    sol = Solution()

    s = "5F3Z-2e-9-w"
    k = 4

    # s = "2-5g-3-J"
    # k = 2

    print(f"Result:   {sol.licenseKeyFormatting(s, k)}")
