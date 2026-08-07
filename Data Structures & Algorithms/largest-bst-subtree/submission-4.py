# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(n: Optional[TreeNode]) -> Tuple(bool, int, int, int):
            nonlocal res
            if not n:
                return (True, 0, float("inf"), -float("inf"))

            lIsBST, lNodes, lmin, lmax = dfs(n.left)
            rIsBST, rNodes, rmin, rmax = dfs(n.right)

            if lIsBST and rIsBST and lmax < n.val and rmin > n.val:
                newSize = lNodes + rNodes + 1
                res = max(res, newSize)
                return (True, newSize, min(lmin, n.val), max(rmax, n.val))

            return (False, 0, 0, 0)

        dfs(root)
        return res



        