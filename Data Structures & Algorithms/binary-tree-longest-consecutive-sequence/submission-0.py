# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 1

        def dfs(curr: Optional[TreeNode], parent: Optional[TreeNode], l: int) -> None:
            nonlocal res
            if not curr:
                return

            if parent and curr.val - parent.val == 1:
                l += 1
            else:
                l = 1
            
            res = max(res, l)

            dfs(curr.left, curr, l)
            dfs(curr.right, curr, l)

            
        dfs(root, None, 1)
        return res