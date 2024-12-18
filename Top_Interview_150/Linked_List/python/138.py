
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            if curr.next:
                old_to_new[curr].next = old_to_new[curr.next]
            else:
                old_to_new[curr].next = None

            if curr.random:
                old_to_new[curr].random = old_to_new[curr.random]
            else:
                old_to_new[curr].random = None

            curr = curr.next

        return old_to_new[head]
