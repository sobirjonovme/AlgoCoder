"""
https://leetcode.com/problems/ransom-note/
"""

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_1 = Counter(ransomNote)
        dict_2 = Counter(magazine)


        for key, value in dict_1.items():
            if key not in dict_2:
                return False
            if value > dict_2[key]:
                return False
        
        return True


if __name__ == '__main__':
    sol = Solution()

    # # example 1
    # ransomNote = "a"
    # magazine = "b"

    # # example 2
    # ransomNote = "aa"
    # magazine = "ab"

    # example 3
    ransomNote = "aa"
    magazine = "aab"

    print(f"Result:   {sol.canConstruct(ransomNote, magazine)}")
