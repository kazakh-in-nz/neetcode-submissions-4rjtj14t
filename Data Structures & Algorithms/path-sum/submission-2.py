# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(n: Optional[TreeNode], localSum: int) -> bool:
            if not n.left and not n.right:
                return localSum + n.val == targetSum

            left = dfs(n.left, localSum + n.val) if n.left else False
            right = dfs(n.right, localSum + n.val) if n.right else False

            return left or right

        return dfs(root, 0)


        