# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def getInorderSuccessor(root):
            while root and root.left:
                root = root.left
            return root

        if not root:
            return root

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            inorderSuccessor = getInorderSuccessor(root.right)

            root.val = inorderSuccessor.val

            root.right = self.deleteNode(root.right, inorderSuccessor.val)

        return root
