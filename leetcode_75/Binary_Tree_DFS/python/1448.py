class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    count = 0

    def count_good_nodes(self, node: TreeNode, mx):

        if node is None:
            return 0

        self.count += int(node.val >= mx)
        mx = max(mx, node.val)

        return self.count_good_nodes(node.left, mx) + self.count_good_nodes(node.right, mx)

    def goodNodes(self, root: TreeNode) -> int:
        self.count_good_nodes(root, -10 ** 5)
        return self.count
