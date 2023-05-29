"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self) -> None:
        self.prev_node = None
        self.min_diff = float('inf')

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        self.minDiffInBST(root.left)

        if self.prev_node is not None:
            self.min_diff = min(self.min_diff, root.val - self.prev_node)
        self.prev_node = root.val

        self.minDiffInBST(root.right)

        return self.min_diff
