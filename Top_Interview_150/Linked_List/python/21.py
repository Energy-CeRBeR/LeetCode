from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        node = head

        left = list1
        right = list2
        while left is not None and right is not None:
            cur_node = None
            if left.val < right.val:
                cur_node = left
                left = left.next
            else:
                cur_node = right
                right = right.next

            if node is None:
                head = cur_node
                node = head
            else:
                node.next = cur_node
                node = node.next

        while left is not None:
            if node is None:
                head = left
                node = head
            else:
                node.next = left
                node = node.next
            left = left.next

        while right is not None:
            if node is None:
                head = right
                node = head
            else:
                node.next = right
                node = node.next
            right = right.next

        return head
