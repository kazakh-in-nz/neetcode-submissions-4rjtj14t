# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        q = deque([(root, root.val)])

        while q:
            q_size = len(q)

            for _ in range(q_size):
                n, prev_max = q.popleft()

                if n.val >= prev_max:
                    count += 1

                new_max = max(n.val, prev_max)

                if n.left:
                    q.append((n.left, new_max)) 
                
                if n.right:
                    q.append((n.right, new_max)) 

        return count
        