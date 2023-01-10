"""
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/
"""


class Solution:
    def isPalindrome(self, word):
        for i in range(len(word)//2):
            if word[i] != word[-(i+1)]:
                return False
            
        return True

    def firstPalindrome(self, words: list[str]) -> str:

        for word in words:
            if self.isPalindrome(word):
                return word
        
        return ""

        
if __name__ == '__main__':
    sol = Solution()

    # words = ["abc","car","ada","racecar","cool"]
    words = ["notapalindrome","racecar"]
    # words = ["def","ghi"]

    print(f"Result:   {sol.firstPalindrome(words)}")
