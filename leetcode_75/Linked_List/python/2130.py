from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = list()
        cur_obj = head
        while cur_obj is not None:
            stack.append(cur_obj.val)
            cur_obj = cur_obj.next

        mx = 0
        size = len(stack)
        for i in range(size // 2):
            mx = max(mx, stack[i] + stack[size - i - 1])

        return mx
