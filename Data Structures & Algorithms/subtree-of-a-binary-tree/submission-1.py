# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def searchSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if not root or not subRoot:
            return False

        return (
            root.val == subRoot.val and 
            self.searchSubtree(root.left, subRoot.left) and 
            self.searchSubtree(root.right, subRoot.right)
            )


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def dfs(n_root: Optional[TreeNode]):
            nonlocal res
            if not n_root or res:
                return

            if n_root.val == subRoot.val:
                if self.searchSubtree(n_root, subRoot):
                    res = True

            dfs(n_root.left)
            dfs(n_root.right)

            
        dfs(root)
        return res