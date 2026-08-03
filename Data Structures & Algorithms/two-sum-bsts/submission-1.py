# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def binarySearch(n: Optional[TreeNode], searchedVal: int) -> bool:
            if not n:
                return False

            if n.val == searchedVal:
                return True
            
            if searchedVal < n.val:
                return binarySearch(n.left, searchedVal)
            else:
                return binarySearch(n.right, searchedVal)

        res = False

        def inorder(n: Optional[TreeNode]):
            nonlocal res
            if not n or res:
                return

            inorder(n.left)
            if not res:
                res = binarySearch(root2, target - n.val)
            inorder(n.right)
        
        inorder(root1)
        return res