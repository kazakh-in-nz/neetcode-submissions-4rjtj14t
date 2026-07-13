# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        output = None

        def dfs(n: TreeNode) -> [bool, bool]:
            nonlocal output
            if not n:
                return [False, False]

            left = dfs(n.left)
            right = dfs(n.right)

            p_found = n.val == p.val or left[0] or right[0]
            q_found = n.val == q.val or left[1] or right[1]

            if not output and p_found and q_found:
                output = n

            return [p_found, q_found]

        dfs(root)
        return output

            

        