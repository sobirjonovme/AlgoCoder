"""
https://leetcode.com/problems/naming-a-company/
"""


class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        result = 0
        letter_goups = [set() for _ in range(26)]

        # 97 -> lowercase a
        for idea in ideas:
            letter_goups[ord(idea[0]) - 97].add(idea[1:])

        for i in range(26):
            for j in range(i+1, 26):
                same_suffixes_num = len(letter_goups[i] & letter_goups[j])
                result += (len(letter_goups[i]) - same_suffixes_num)\
                    * (len(letter_goups[j]) - same_suffixes_num)

        return 2 * result


if __name__ == '__main__':
    sol = Solution()

    ideas = ["coffee","donuts","time","toffee"]
    # ideas = ["lack","back"]

    print(f"Result:   {sol.distinctNames(ideas)}")
