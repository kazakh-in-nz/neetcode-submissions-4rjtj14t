# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []

        q = deque([root])

        while q:
            level_size = len(q)

            for i in range(level_size):
                n = q.popleft()

                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)

                if i == level_size - 1:
                    res.append(n.val)

        return res



            

        