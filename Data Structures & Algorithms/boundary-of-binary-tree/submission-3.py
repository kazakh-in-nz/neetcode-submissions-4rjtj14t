# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def getLeftEdge(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(n: Optional[TreeNode]):
            nonlocal res
            if not n or (not n.left and not n.right):
                return

            res.append(n.val)
            
            if n.left:
                dfs(n.left)
            elif n.right:
                dfs(n.right)

        dfs(root.left)
        return res

    def getLeafs(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(n: Optional[TreeNode]):
            nonlocal res
            if not n:
                return

            if not n.left and not n.right:
                res.append(n.val)

            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return res

    def getRightEdge(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def dfs(n: Optional[TreeNode]):
            nonlocal res
            if not n or (not n.left and not n.right):
                return

            res.append(n.val)
            
            if n.right:
                dfs(n.right)
            elif n.left:
                dfs(n.left)

        dfs(root.right)
        return res

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        left = self.getLeftEdge(root)
        center = self.getLeafs(root)
        right = self.getRightEdge(root)

        res = [root.val]
        res.extend(left)
        res.extend(center)
        res.extend(right[::-1])

        return res

            

