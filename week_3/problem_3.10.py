"""
https://leetcode.com/problems/fizz-buzz/
"""


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = [str]*n

        for i in range(1, n+1):
            temp = ''
            if i%3 == 0:
                temp += 'Fizz'
            if i%5 == 0:
                temp += 'Buzz'
            
            if temp:
                result[i-1] = temp
                continue

            result[i-1] = str(i)

        return result


if __name__ == '__main__':
    sol = Solution()

    n = 3
    n = 5
    n = 15

    print(f"Result:   {sol.fizzBuzz(n)}")
