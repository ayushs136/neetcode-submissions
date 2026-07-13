# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []

        q = deque([root] if root else [])

        while q:
            level = []

            for i in range(len(q)):
                curr = q.popleft()

                level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level = reversed(level) if len(res) % 2 else level
            res.append(level)

        return res
