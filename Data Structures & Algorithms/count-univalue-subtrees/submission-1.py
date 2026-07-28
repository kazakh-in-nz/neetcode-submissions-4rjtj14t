# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        def dfs(n: Optional[TreeNode]) -> bool:
            nonlocal res
            if not n:
                return True

            left = dfs(n.left)
            right = dfs(n.right)

            if not left or not right:
                return False

            if n.left and n.val != n.left.val:
                return False

            if n.right and n.val != n.right.val:
                return False

            res += 1
            return True

        dfs(root)
        return res