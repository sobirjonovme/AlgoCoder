"""
https://leetcode.com/problems/student-attendance-record-i/
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        absent_counter = 0
        late_counter = 0

        for i in s:          
            if i == 'L':
                late_counter += 1
                if late_counter >= 3:
                    return False
                continue
            late_counter = 0

            if i == 'A':
                absent_counter += 1
                if absent_counter >= 2:
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()

    s = "PPALLP"
    # s = "PPALLL"

    print(f"Result:   {sol.checkRecord(s)}")
