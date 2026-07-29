# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        stack = [(root, False, 0)]

        while stack:
            node, visited, accum = stack.pop()

            if node:
                if visited:
                    if accum == targetSum and not node.left and not node.right:
                        return True
                else:
                    stack.append((node, True, accum + node.val ))

                    if node.right:
                        stack.append((node.right, False, accum + node.val))    
                    
                    if node.left:
                        stack.append((node.left, False, accum + node.val))    

        
        return False