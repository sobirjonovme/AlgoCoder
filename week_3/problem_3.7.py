"""
https://leetcode.com/problems/goal-parser-interpretation/
"""


class Solution:
    def interpret(self, command: str) -> str:
        result = ''

        for i in range(len(command)):
            if command[i] == 'G':
                result += 'G'
                continue

            if command[i] == ')':
                if command[i-1] == '(':
                    result += 'o'
                    continue
                result += 'al'
        
        return result


if __name__ == '__main__':
    sol = Solution()

    # command = "G()(al)"
    # command = "G()()()()(al)"
    command = "(al)G(al)()()G"

    print(f"Result:   {sol.interpret(command)}")

