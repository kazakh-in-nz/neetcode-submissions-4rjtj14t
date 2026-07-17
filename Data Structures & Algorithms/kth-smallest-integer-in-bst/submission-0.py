# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        
        def dfs(n: Optional[TreeNode]) -> int:
            nonlocal res

            if not n or len(res) > k:
                return

            dfs(n.left)           
            res.append(n.val) 
            dfs(n.right)

        dfs(root)
        return res[k-1]