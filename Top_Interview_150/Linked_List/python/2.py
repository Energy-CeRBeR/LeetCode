from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode((l1.val + l2.val) % 10)
        ost = (l1.val + l2.val) // 10
        cur_node = head

        l1 = l1.next
        l2 = l2.next
        while l1 is not None and l2 is not None:
            cur_node.next = ListNode(((l1.val + l2.val + ost) % 10))
            ost = (l1.val + l2.val + ost) // 10
            l1 = l1.next
            l2 = l2.next
            cur_node = cur_node.next

        while l1 is not None:
            cur_node.next = ListNode((l1.val + ost) % 10)
            ost = (l1.val + ost) // 10
            l1 = l1.next
            cur_node = cur_node.next

        while l2 is not None:
            cur_node.next = ListNode((l2.val + ost) % 10)
            ost = (l2.val + ost) // 10
            l2 = l2.next
            cur_node = cur_node.next

        if ost:
            cur_node.next = ListNode(ost)

        return head
