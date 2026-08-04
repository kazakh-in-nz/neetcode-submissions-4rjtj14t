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

        stack = [(root, False)]

        while stack:
            curr, visited = stack.pop()
            
            if visited:
                res.append(curr.val)
            else:
                stack.append((curr, True))

                if len(curr.children or []) > 0:
                    for i in range(len(curr.children)-1, -1, -1):
                        stack.append((curr.children[i], False))

        return res