# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        def dfs(root, p, q):

            if root is None or root.val == p.val or root.val == q.val:
                return root

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)

            if left is None:
                return right
            elif right is None:
                return left
            else:
                return root

        return dfs(root, p, q)
