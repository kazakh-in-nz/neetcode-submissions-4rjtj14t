# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res = -float("inf")

        def dfs(n: Optional[TreeNode]):
            nonlocal res
            if not n:
                return (0, 0)

            l_ave, l_nodes = dfs(n.left)
            r_ave, r_nodes = dfs(n.right)

            total_nodes = l_nodes + r_nodes + 1
            total_sum = l_ave * l_nodes + n.val + r_ave * r_nodes
            new_avg = total_sum / total_nodes

            res = max(res, new_avg)        

            return (new_avg, total_nodes)

        dfs(root)
        return res