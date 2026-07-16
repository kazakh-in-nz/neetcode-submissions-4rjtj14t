# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(n: Optional[TreeNode], low: float, high: float):
            nonlocal res

            if not n or not res:
                return None

            if not (low < n.val < high):
                res = False
                return

            dfs(n.left, low, n.val)
            dfs(n.right, n.val, high)
            
        dfs(root, -float("inf"), float("inf"))
        return res