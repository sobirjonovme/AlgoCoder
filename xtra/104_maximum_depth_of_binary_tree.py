"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
        
#         left_side = self.maxDepth(root.left)
#         right_side = self.maxDepth(root.right)

#         return max(left_side, right_side) + 1
