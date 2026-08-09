"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        res = 0

        if not root:
            return res

        def dfs(n: 'Node') -> int:
            nonlocal res

            first_lgst = 0
            second_lgst = 0

            for ch in n.children:
                chOutput = dfs(ch)
                
                if chOutput > first_lgst:
                    second_lgst = first_lgst
                    first_lgst = chOutput
                elif chOutput > second_lgst:
                    second_lgst = chOutput

            res = max(res, first_lgst + second_lgst)

            return max(first_lgst, second_lgst) + 1

        dfs(root)
        return res