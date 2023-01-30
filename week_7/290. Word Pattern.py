"""
https://leetcode.com/problems/word-pattern/
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')

        if len(words) != len(pattern):
            return False

        words_set = set()
        pattern_dict = {}

        for i in range(len(pattern)):
            if pattern[i] in pattern_dict:
                if pattern_dict[pattern[i]] != words[i]:
                    return False
                continue

            if words[i] in words_set:
                return False
            
            pattern_dict[pattern[i]] = words[i]
            words_set.add(words[i])
        
        return True


if __name__ == '__main__':
    sol = Solution()

    # example 1
    pattern = "abba"
    s = "dog cat cat dog"

    # # example 2
    # pattern = "abba"
    # s = "dog cat cat fish"

    # # example 3
    # pattern = "aaaa"
    # s = "dog cat cat dog"

    print(f"Result:   {sol.wordPattern(pattern, s)}")
