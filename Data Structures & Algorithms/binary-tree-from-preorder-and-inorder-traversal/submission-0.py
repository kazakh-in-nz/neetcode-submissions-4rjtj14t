# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        r_val = preorder[0]
        mid = inorder.index(r_val)

        node = TreeNode(r_val)

        left = self.buildTree(preorder[1:mid+1], inorder[0:mid])
        right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        node.left = left
        node.right = right

        return node



