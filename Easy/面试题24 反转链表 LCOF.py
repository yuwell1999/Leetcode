# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # first为新链表头结点
        first = None
        cur = head

        while cur is not None:
            # 摘下节点头插法到新链表
            tmp = cur.next
            cur.next = first
            first = cur
            cur = tmp

        return first
