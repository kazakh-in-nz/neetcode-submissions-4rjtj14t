# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(n: Optional[TreeNode], d: int) -> int:
            if not n:
                return d
            
            d += 1

            left_d = dfs(n.left, d)
            right_d = dfs(n.right, d)

            return max(d, left_d, right_d)

        return dfs(root, 0)
        