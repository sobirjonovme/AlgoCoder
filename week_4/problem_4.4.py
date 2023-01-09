"""
https://leetcode.com/problems/repeated-substring-pattern/
"""


class Solution:
    def is_valid(self, substring: str, s: str):
        
        for i in range(0, len(s), len(substring)):
            for j in range(len(substring)):
                if substring[j] != s[i+j]:
                    return False
        
        return True
                

    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        guess = ''

        for i in range(length//2):
            guess += s[i]

            if length % (i+1) == 0:
                if self.is_valid(guess, s):
                    return True
        
        return False



if __name__ == '__main__':
    sol = Solution()

    s = "abab"
    # s = "aba"
    # s = "abcabcabcabc"

    print(f"Result:   {sol.repeatedSubstringPattern(s)}")
