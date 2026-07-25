# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def dfs(n: Optional[TreeNode]) -> List[int]:
            nonlocal res
            if not root:
                return [0, 0]

            inc = dcr = 1

            if n.left:
                left = dfs(n.left)

                if (n.val == n.left.val + 1):
                    dcr = left[1] + 1
                elif (n.val + 1 == n.left.val):
                    inc = left[0] + 1

            if n.right:
                right = dfs(n.right)

                if (n.val == n.right.val + 1):
                    dcr = max(dcr, right[1] + 1)
                elif (n.val + 1 == n.right.val):
                    inc = max(inc, right[0] + 1)

            res = max(res, dcr + inc - 1)
            return [inc, dcr]





            
            return local_inc, local_decd

        dfs(root)
        return res