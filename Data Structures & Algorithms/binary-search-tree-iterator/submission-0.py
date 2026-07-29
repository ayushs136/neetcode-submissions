# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.pointer = -1
        self.inorder = []

        def inorder(root, res):
            if not root:
                return
            inorder(root.left, res)
            res.append(root.val)
            inorder(root.right, res)

        inorder(root, self.inorder)

    def next(self) -> int:
        self.pointer += 1
        return self.inorder[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer + 1 < len(self.inorder)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
