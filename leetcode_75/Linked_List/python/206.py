from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return

        if head.next is None:
            return head

        prev = None
        cur = head
        next = cur.next
        cur.next = prev
        while next is not None:
            prev = cur
            cur = next
            next = cur.next
            cur.next = prev

        return cur
