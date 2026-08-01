"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        q = deque([root, None])
        prev = None
        while q:

            for _ in range(len(q)):
                curr = q.popleft()
                if curr:
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
                    if prev:
                        prev.next = curr
                else:
                    if len(q) == 0:
                        break
                    q.append(None)
                prev = curr

        return root
