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

        def dfs(n: Optional[TreeNode], level: int):
            nonlocal output

            if not n:
                return

            if len(output) - 1 < level:
                output.append([n.val])
            else:
                output[level].append(n.val)

            dfs(n.left, level + 1)
            dfs(n.right, level + 1)

        dfs(root, 0)
        return output