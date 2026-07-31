# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None

        def inorder(root):

            if not root:
                return

            inorder(root.left)

            if self.prev and root.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = root

            self.prev = root
            inorder(root.right)

        inorder(root)
        if self.first and self.second:
            self.first.val, self.second.val = self.second.val, self.first.val
