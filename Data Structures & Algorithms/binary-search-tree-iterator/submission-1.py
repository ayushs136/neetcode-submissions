# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._store_left_nodes(root)

    def next(self) -> int:
        node = self.stack.pop()

        if node and node.right:
            self._store_left_nodes(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _store_left_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
