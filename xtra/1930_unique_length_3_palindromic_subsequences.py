"""
https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
"""
import string


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0

        for char in string.ascii_lowercase:
            left, right = s.find(char), s.rfind(char)
            if left != -1 and left != right:
                count += len(set(s[left+1:right]))

        return count
