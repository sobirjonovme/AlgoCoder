"""
https://leetcode.com/problems/flipping-an-image/
"""


class Solution:
    def invertPoint(self, point):
        return (point+1) % 2
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        
        for row in image:
            length = len(row)
            for i in range(length//2):
                row[i], row[-(i+1)] = self.invertPoint(row[-(i+1)]), self.invertPoint(row[i])
            
            if length%2 == 1:
                row[length//2] = self.invertPoint(row[length//2])
        
        return image


if __name__ == '__main__':
    sol = Solution()

    image = [[1,1,0],[1,0,1],[0,0,0]]
    image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]

    print(f"Result:   {sol.flipAndInvertImage(image)}")