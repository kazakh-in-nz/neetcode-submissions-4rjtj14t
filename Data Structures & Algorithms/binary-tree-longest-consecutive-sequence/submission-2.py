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

        def dfs(curr: Optional[TreeNode], parent: Optional[TreeNode], l: int) -> int:
            if not curr:
                return 0

            if parent and curr.val - parent.val == 1:
                l += 1
            else:
                l = 1

            left = dfs(curr.left, curr, l)
            right = dfs(curr.right, curr, l)

            return max(l, left, right)
            
        res = dfs(root, None, 1)
        return res