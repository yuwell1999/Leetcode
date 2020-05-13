# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not len(nums):
            return None

        newNode = TreeNode(nums[len(nums) // 2])

        newNode.left = self.sortedArrayToBST(nums[:len(nums) // 2])
        newNode.right = self.sortedArrayToBST(nums[(len(nums) // 2) + 1:])

        return newNode
