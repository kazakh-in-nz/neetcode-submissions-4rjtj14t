# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []

        def dfs(r: Optional[TreeNode]) -> None:
            if not r:
                return
            
            dfs(r.left)
            output.append(r.val)
            dfs(r.right)

        dfs(root)
        return output

        