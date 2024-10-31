from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur_node = head

        size = 0
        while cur_node is not None:
            cur_node = cur_node.next
            size += 1

        prev_ind = size - n
        count = 0
        cur_node = head
        while count < prev_ind:
            cur_node = cur_node.next
            count += 1

        if cur_node is not None:
            cur_node.next = cur_node.next.next if cur_node.next.next else None

        return head
