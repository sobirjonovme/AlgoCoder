"""
https://leetcode.com/problems/merge-strings-alternately/
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ''
        length1 = len(word1)
        length2 = len(word2)

        min_length = min(length1, length2)

        for i in range(min_length):
            result += word1[i] + word2[i]
        
        for i in range(min_length, length1):
            result += word1[i]
        
        for i in range(min_length, length2):
            result += word2[i]
        
        return result


if __name__ == '__main__':
    sol = Solution()

    # # example 1
    # word1 = "abc"
    # word2 = "pqr"

    # example 2
    word1 = "ab"
    word2 = "pqrs"

    # # example 3
    # word1 = "abcd"
    # word2 = "pq"

    print(f"Result:   {sol.mergeAlternately(word1, word2)}")
