# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> None|int:
            if not p and not q:
                return 0
            elif (not p and q) or (p and not q):
                return -1
            
            if p.val != q.val:
                return -1

            left = dfs(p.left, q.left)
            if left == -1:
                return -1

            right = dfs(p.right, q.right)
            if right == -1:
                return -1

        return dfs(p, q) != -1
        