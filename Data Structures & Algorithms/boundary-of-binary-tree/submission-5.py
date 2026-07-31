# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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
            else:
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
            else:
                dfs(n.left)

        dfs(root)
        return res
    
    def getCenterEdge(self, root: Optional[TreeNode]) -> List[int]:
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
    
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = [root.val]
        
        if not root.left and not root.right:
            return res
        
        left = self.getLeftEdge(root.left)
        center = self.getCenterEdge(root)
        right = self.getRightEdge(root.right)

        res.extend(left)
        res.extend(center)
        res.extend(right[::-1])

        return res