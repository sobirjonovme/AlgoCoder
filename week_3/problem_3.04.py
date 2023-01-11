"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""


class Solution:
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    def halvesAreAlike(self, s: str) -> bool:
        length = len(s)

        counter_1, counter_2 = 0, 0

        for i in range(length//2):
            if s[i] in self.vowels:
                counter_1 += 1

        for i in range(length//2, length):
            if s[i] in self.vowels:
                counter_2 += 1

        return counter_1 == counter_2



if __name__ == '__main__':
    sol = Solution()

    # s = "book"
    s = "textbook"

    print(f"Result: {sol.halvesAreAlike(s)}")
