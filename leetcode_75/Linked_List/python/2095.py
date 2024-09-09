from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __get_length(self, head: Optional[ListNode]) -> int:
        cur = head
        n = 1
        while cur.next is not None:
            cur = cur.next
            n += 1

        return n

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = self.__get_length(head)
        if n == 1:
            return

        middle = n // 2

        prev = None
        cur = head
        next = cur.next
        k = 0
        while k != middle:
            prev = cur
            cur = next
            next = cur.next
            k += 1


        if next is not None:
            prev.next = next
        else:
            prev.next = None

        return head