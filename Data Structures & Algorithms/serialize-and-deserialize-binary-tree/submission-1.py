# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res, q = [], deque([root])

        while q:
            curr = q.popleft()

            if curr:
                res.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                res.append("null")

        # Trim trailing "null" values to save space
        while res and res[-1] == "null":
            res.pop()

        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
            
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        n = len(vals)
        while q and i < n:
            curr = q.popleft()

            if i < n and vals[i] != "null":
                curr.left = TreeNode(int(vals[i]))
                q.append(curr.left)
            i += 1
            if i < n and vals[i] != "null":
                curr.right = TreeNode(int(vals[i]))
                q.append(curr.right)

            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
