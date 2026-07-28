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

            isUnivalue = left and right

            if not isUnivalue:
                return False

            if n.left and n.right:
                isUnivalue = n.val == n.left.val == n.right.val
            elif n.left:
                isUnivalue = n.val == n.left.val
            elif n.right:
                isUnivalue = n.val == n.right.val
            
            if isUnivalue:
                res += 1

            return isUnivalue

        dfs(root)
        return res

                
        