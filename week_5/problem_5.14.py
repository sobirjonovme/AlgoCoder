"""
https://leetcode.com/problems/valid-palindrome-ii/
"""


class Solution:
    @staticmethod
    def validPalindrome_II(s, left, right):
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -=1
        
        if left < right:
            return self.validPalindrome_II(s, left+1, right) or self.validPalindrome_II(s, left, right-1)
        
        return True


if __name__ == '__main__':
    sol = Solution()

    # s = "aba"
    s = "abca"
    s = "abc"

    print(f"Result:   {sol.validPalindrome(s)}")
