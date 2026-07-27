# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict, deque

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        m = defaultdict(list)
        q = deque()
        q.append((root, 0))

        while q:
            q_size = len(q)

            for _ in range(q_size):
                n, coordinate = q.popleft()
                m[coordinate].append(n.val)

                if n.left:
                    q.append((n.left, coordinate - 1))

                if n.right:
                    q.append((n.right, coordinate + 1))

        keys = list(m.keys())
        keys.sort()

        return [m[key] for key in keys]