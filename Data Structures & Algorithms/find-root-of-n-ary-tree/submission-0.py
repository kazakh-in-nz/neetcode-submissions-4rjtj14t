"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        if len(tree) == 0:
            return None
        elif len(tree) == 1:
            return tree[0]

        children = set()
        
        for n in tree:
            for ch in n.children:
                children.add(ch.val)

        for n in tree:
            if len(n.children) > 0 and n.val not in children:
                return n