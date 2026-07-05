# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        
        def dfs(r: Optional[TreeNode]) -> None:
            if not r:
                return

            output.append(r.val)
            dfs(r.left)
            dfs(r.right)

        dfs(root)
        return output