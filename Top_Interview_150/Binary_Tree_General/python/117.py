class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        head = root

        while head:
            temp = Node()
            cur = temp

            while head:
                if head.left:
                    cur.next = head.left
                    cur = cur.next

                if head.right:
                    cur.next = head.right
                    cur = cur.next

                head = head.next

            head = temp.next

        return root
