"""
https://leetcode.com/problems/reverse-prefix-of-word/
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        result_word = ''
        is_found = False

        for i in word:
            result_word += i
            if i == ch and is_found is False:
                result_word = result_word[::-1]
                is_found = True
        
        return result_word


if __name__ == '__main__':
    sol = Solution()

    # # example 1
    # word = "abcdefd"
    # ch = "d"

    # # example 2
    # word = "xyxzxe"
    # ch = "z"

    # example 3
    word = "abcd"
    ch = "z"

    print(f"Result:   {sol.reversePrefix(word, ch)}")
