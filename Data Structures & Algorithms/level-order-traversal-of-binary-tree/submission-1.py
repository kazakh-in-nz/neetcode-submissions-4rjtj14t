# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        if not root:
            return output

        q = deque([root])

        while q:
            level = []

            for i in range(len(q)):
                n = q.popleft()
                level.append(n.val)

                if n.left:
                    q.append(n.left)

                if n.right:
                    q.append(n.right)

            output.append(level)
        
        return output