"""
https://leetcode.com/problems/detect-capital/
"""

# A-Z  ->  65-90
# a-z  ->  97-122


class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) == 1:
            return True

        if (97 <= ord(word[0])) or (97 <= ord(word[1])):
            for i in range(1, len(word)):
                if ord(word[i]) < 97:
                    return False
        
            return True
        
        for i in range(2, len(word)):
            if 97 <= ord(word[i]):
                return False
        
        return True


if __name__ == '__main__':
    sol = Solution()

    word = "USA"
    # word = "FlaG"

    print(f"Result:   {sol.detectCapitalUse(word)}")
