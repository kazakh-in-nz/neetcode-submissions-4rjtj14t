from collections import defaultdict

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        lookup_in = defaultdict()
        for i, v in enumerate(inorder):
            lookup_in[v] = i

        pre_idx = 0
        def formTree(left_in: int, right_in: int) -> Optional[TreeNode]:
            nonlocal pre_idx
            if left_in > right_in:
                return None

            val = preorder[pre_idx]
            mid = lookup_in.get(val)
            n = TreeNode(val)
            
            pre_idx += 1
            n.left = formTree(left_in, mid - 1)
            n.right = formTree(mid + 1, right_in)

            return n

        return formTree(0, len(inorder) - 1)