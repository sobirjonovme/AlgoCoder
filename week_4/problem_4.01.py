"""
https://leetcode.com/problems/longest-common-prefix/
"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''

        for i in range(len(strs[0])):
            is_same = True

            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[0][i] != strs[j][i]:
                    is_same = False
                    break
            
            if is_same is False:
                break

            result += strs[0][i]
        
        return result



if __name__ == '__main__':
    sol = Solution()

    # strs = ["flower","flow","flight"]
    strs = ["dog","racecar","car"]

    print(f"Result:   {sol.longestCommonPrefix(strs)}")
