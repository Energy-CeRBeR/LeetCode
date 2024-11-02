from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        over_dummy = ListNode(0)

        head_node = head
        result_node = dummy
        over_node = over_dummy
        while head_node is not None:
            if head_node.val < x:
                result_node.next = head_node
                result_node = result_node.next
            else:
                over_node.next = head_node
                over_node = over_node.next
            head_node = head_node.next
        result_node.next = None
        over_node.next = None

        over_node = over_dummy.next
        while over_node is not None:
            result_node.next = over_node
            result_node = result_node.next
            over_node = over_node.next

        return dummy.next
