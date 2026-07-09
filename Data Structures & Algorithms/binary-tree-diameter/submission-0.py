# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0

        def dfs(n: Optional[TreeNode]) -> int:
            nonlocal res

            if not n:
                return 0

            left = dfs(n.left)
            right = dfs(n.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res