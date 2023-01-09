"""
https://leetcode.com/problems/consecutive-characters/
"""


class Solution:
    def maxPower(self, s: str) -> int:
        power = 0
        substring_length = 1
        ch = s[0]

        for i in range(1, len(s)):
            print(substring_length)
            print(s[i], end='  ')
            if s[i] == ch:
                substring_length += 1
                continue

            if substring_length > power:
                power = substring_length
            
            substring_length = 1
            ch = s[i]
        
        if substring_length > power:
            power = substring_length
        
        return power


if __name__ == '__main__':
    sol = Solution()

    # s = "leetcode"
    # s = "abbcccddddeeeeedcba"
    # s = "triplepillooooow"
    s = "ccbccbb"

    print(f"Result:   {sol.maxPower(s)}")
