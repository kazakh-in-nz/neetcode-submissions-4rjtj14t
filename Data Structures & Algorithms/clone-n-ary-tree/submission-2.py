"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        clone = Node(root.val)
        s = [(root, clone)]

        while s:
            n, copy = s.pop()

            for child in n.children:
                childCopy = Node(child.val)
                copy.children.append(childCopy)
                s.append((child, childCopy))

        return clone
        