"""
https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
"""


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        input_words = text.split()
        result_words = []

        for i in range(len(input_words)-2):
            if input_words[i] == first and input_words[i+1] == second:
                result_words.append(input_words[i+2])
        
        return result_words


if __name__ == '__main__':
    sol = Solution()

    # # first example
    # text = "alice is a good girl she is a good student"
    # first = "a"
    # second = "good"

    # second example
    text = "we will we will rock you"
    first = "we"
    second = "will"

    print(f"Result:   {sol.findOcurrences(text, first, second)}")
