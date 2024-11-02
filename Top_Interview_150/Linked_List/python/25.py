from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        ptr = dummy

        while ptr is not None:
            tracker = ptr

            for _ in range(k):
                tracker = tracker.next
                if tracker is None:
                    return dummy.next

            previous, current = self.reverseLinkedList(ptr.next, k)

            lastNodeOfReversedGroup = ptr.next
            lastNodeOfReversedGroup.next = current
            ptr.next = previous
            ptr = lastNodeOfReversedGroup

        return dummy.next

    def reverseLinkedList(self, head: ListNode, k: int) -> Tuple[ListNode, ListNode]:
        previous = None
        current = head

        for _ in range(k):
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous, current
