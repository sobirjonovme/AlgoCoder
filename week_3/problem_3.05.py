"""
https://leetcode.com/problems/increasing-decreasing-string/
"""


class Solution:
    def sortString(self, s: str) -> str:
        result = ''

        abc_freq = dict()
        for i in s:
            abc_freq[i] = abc_freq.get(i, 0) + 1
        abc_list = list(abc_freq.keys())
        abc_list.sort()

        while True:
            is_continued = False
            for i in abc_list:
                if abc_freq[i] == 0:
                    continue
                result += i
                abc_freq[i] -= 1
                is_continued = True
            if is_continued is False:
                break

            is_continued = False
            for i in range(len(abc_list)-1, -1, -1):
                letter = abc_list[i]
                if abc_freq[letter] == 0:
                    continue
                result += letter
                abc_freq[letter] -= 1
                is_continued = True
            if is_continued is False:
                break
        
        return result
            



if __name__ == '__main__':
    sol = Solution()

    s = "aaaabbbbcccc"
    s = "rat"

    print(f"Result:   {sol.sortString(s)}")


