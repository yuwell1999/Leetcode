# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            left_max = self.maxDepth(root.left)
            right_max = self.maxDepth(root.right)
            return max(left_max, right_max) + 1
