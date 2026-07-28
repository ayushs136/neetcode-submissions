# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def preorder(root, mini, maxi):
            if not root:
                return True

            if mini >= root.val or root.val >= maxi:
                return False
            left = preorder(root.left, mini, root.val)
            right = preorder(root.right, root.val, maxi)

            return left and right

        return preorder(root, float("-inf"), float("inf"))