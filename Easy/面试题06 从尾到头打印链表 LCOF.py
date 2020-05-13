# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        lst = []

        def dfs(node):
            if node:
                dfs(node.next)
                lst.append(node.val)

        dfs(head)

        return lst
