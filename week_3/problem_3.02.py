"""
https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
"""

class Solution:
    def numOfStrings(self, patterns: list[str], word: str) -> int:
        counter = 0

        for ptrn in patterns:
            if ptrn in word:
                counter += 1
        
        return counter


if __name__ == '__main__':
    sol = Solution()

    # patterns = ["a", "abc", "bc", "d"]
    # word = "abc"

    # patterns = ["a", "b", "c"]
    # word = "aaaaabbbbb"

    patterns = ["a", "a", "a"]
    word = "ab"

    print(f"Result:   {sol.numOfStrings(patterns, word)}")
