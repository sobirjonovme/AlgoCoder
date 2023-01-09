"""
https://leetcode.com/problems/sorting-the-sentence/
"""


class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(' ')

        result_words = [str]*len(words)

        for word in words:
            result_words[int(word[-1])-1] = word[:-1]

        return ' '.join(result_words)


if __name__ == '__main__':
    sol = Solution()

    # s = "is2 sentence4 This1 a3"
    s = "Myself2 Me1 I4 and3"

    print(f"Result:   {sol.sortSentence(s)}")
