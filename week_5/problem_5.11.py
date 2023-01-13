"""
https://leetcode.com/problems/reverse-vowels-of-a-string/
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s_vowels = []
        result = ''

        for i in s:
            if i.lower() in vowels:
                s_vowels.append(i)
        
        for i in s:
            if i.lower() in vowels:
                result += s_vowels.pop()
                continue
            result += i
        
        return result
                


if __name__ == '__main__':
    sol = Solution()

    s = "hello"
    s = "leetcode"

    print(f"Result:   {sol.reverseVowels(s)}")
