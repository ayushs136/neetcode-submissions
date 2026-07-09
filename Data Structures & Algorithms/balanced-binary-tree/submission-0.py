# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):

            if not root:
                return 0

            return 1 + max(height(root.left), height(root.right))

        if not root:
            return True

        leftH = height(root.left)
        rightH = height(root.right)

        if abs(leftH - rightH) > 1:
            return False

        leftBalanced = self.isBalanced(root.left)
        rightBalanced = self.isBalanced(root.right)

        if not leftBalanced or not rightBalanced:
            return False

        return True