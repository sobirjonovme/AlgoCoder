"""
https://leetcode.com/problems/string-matching-in-an-array/
"""


class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result_words = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    result_words.append(words[i])
                    break
        
        return result_words


if __name__ == '__main__':
    sol = Solution()

    # # example 1
    # words = ["mass","as","hero","superhero"]

    # # example 2
    # words = ["leetcode","et","code"]

    # example 3
    words = ["blue","green","bu"]

    print(f"Result:   {sol.stringMatching(words)}")
