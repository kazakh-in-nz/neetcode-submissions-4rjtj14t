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
            return res

        q = deque([root])

        while q:
            l = len(q)

            for i in range(l):
                n = q.popleft()

                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)

                if i == l - 1:
                    res.append(n.val)

        return res



            

        