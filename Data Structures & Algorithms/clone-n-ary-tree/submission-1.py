"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        clone = Node(root.val)
        s = [(root, False, None, clone, None)]

        while s:
            n, is_visited, parent, copy, copyParent = s.pop()

            if is_visited:
                if parent:
                    copyParent.children.append(copy)
            else:
                s.append((n, True, parent, copy, copyParent))
                
                for i in range(len(n.children)-1,-1,-1):
                    child = n.children[i]
                    print(child.val)
                    s.append((child, False, n, Node(child.val), copy))


        return clone
        