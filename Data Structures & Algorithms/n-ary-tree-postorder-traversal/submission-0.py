"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        if not root:
            return res

        def dfs(n):
            nonlocal res

            if not n:
                return

            for ch in n.children:
                dfs(ch)

            res.append(n.val)

        dfs(root)
        return res