"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_set = set()
        longest_length = 0
        left, right = 0, 0

        while right < len(s):
            
            if s[right] not in sub_set:
                sub_set.add(s[right])
                right += 1
                longest_length = max(longest_length, right-left)
                continue
            
            sub_set.remove(s[left])
            left += 1

        return longest_length
                

if __name__ == '__main__':
    sol = Solution()

    s = "abcabcbb"
    # s = "bbbbb"
    # s = "pwwkew"

    print(f"Result:   {sol.lengthOfLongestSubstring(s)}")
