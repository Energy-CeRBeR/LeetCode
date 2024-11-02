from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur_node = head
        nodes: List[ListNode] = []
        while cur_node:
            nodes.append(cur_node)
            cur_node = cur_node.next

        n = len(nodes)
        if n == 0:
            return None
        k %= n

        dummy = ListNode(0)
        cur_node = dummy
        for i in range(n):
            cur_node.next = nodes[(i + k) % n]
            cur_node = cur_node.next
        cur_node.next = None

        return dummy.next
