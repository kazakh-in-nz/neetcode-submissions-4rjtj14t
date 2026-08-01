# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def removeLeafs(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(n: Optional[TreeNode]) -> bool:
            nonlocal res

            if not n:
                return False

            if not n.left and not n.right:
                res.append(n.val)
                return True

            isLeftLeaf = dfs(n.left)
            isRightLeaf = dfs(n.right)

            if n.left and isLeftLeaf:
                n.left = None
            
            if n.right and isRightLeaf:
                n.right = None

        dfs(root)
        return res


    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        while root.left or root.right:
            output = self.removeLeafs(root)
            res.append(output)

        res.append([root.val])
        return res

        