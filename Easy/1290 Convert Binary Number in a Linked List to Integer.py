# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        sum = 0
        while head:
            sum *= 2
            sum += head.val
            head = head.next
        return sum
