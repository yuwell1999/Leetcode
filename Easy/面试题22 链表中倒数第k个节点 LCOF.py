# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = slow = head

        for i in range(0, k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow
