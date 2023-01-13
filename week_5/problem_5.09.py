"""
https://leetcode.com/problems/reverse-string/
"""


class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]

        return s


if __name__ == '__main__':
    sol = Solution()

    s = ["h", "e", "l", "l", "o"]
    # s = ["H", "a", "n", "n", "a", "h"]

    print(f"Result:   {sol.reverseString(s)}")
