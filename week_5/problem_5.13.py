"""
https://leetcode.com/problems/valid-palindrome/
"""


class Solution:
    @staticmethod
    def isAlphanumeric(ch):
        ascii_code = ord(ch)
        
        if 48 <= ascii_code and ascii_code <= 57:
            return True
        if 65 <= ascii_code and ascii_code <= 90:
            return True
        if 97 <= ascii_code and ascii_code <= 122:
            return True
        
        return False
        
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if self.isAlphanumeric(s[left]) is False:
                left += 1
                continue
            if self.isAlphanumeric(s[right]) is False:
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True
            

if __name__ == '__main__':
    sol = Solution()

    # examples
    s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    # s = " "

    print(f"Result:   {sol.isPalindrome(s)}")
