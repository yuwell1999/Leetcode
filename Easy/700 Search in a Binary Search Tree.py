# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Recursive
        # if root is None or root.val == val:
        #     return root
        #
        # return self.searchBST(root.left, val) if root.val > val else self.searchBST(root.right, val)

        # Iteration
        while root is not None or root.val != val:
            root = root.left if val < root.val else root.right

        return root
