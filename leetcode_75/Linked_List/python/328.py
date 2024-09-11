from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_head = None
        even_head = None
        cur_odd_obj = None
        cur_even_obj = None
        cur_obj = head
        cur_ind = 1
        while cur_obj is not None:
            next_obj = cur_obj.next
            cur_obj.next = None
            if cur_ind % 2 != 0:
                if odd_head is not None:
                    cur_odd_obj.next = cur_obj
                    cur_odd_obj = cur_obj
                else:
                    odd_head = cur_obj
                    cur_odd_obj = odd_head
            else:
                if even_head is not None:
                    cur_even_obj.next = cur_obj
                    cur_even_obj = cur_obj
                else:
                    even_head = cur_obj
                    cur_even_obj = cur_obj

            cur_obj = next_obj
            cur_ind += 1

        if cur_odd_obj is not None:
            cur_odd_obj.next = even_head

        return odd_head
