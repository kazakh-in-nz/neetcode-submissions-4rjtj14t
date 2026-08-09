"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""
import heapq

class Solution:
    def diameter(self, root: 'Node') -> int:
        res = 0

        if not root:
            return res

        def dfs(n: 'Node') -> int:
            nonlocal res
            if not n:
                return 0

            childRes = []
            for ch in n.children:
                chOutput = dfs(ch)
                heapq.heappush(childRes, chOutput * -1)

            top_two = []
            for _ in range(2):
                if childRes:
                    top_two.append(-heapq.heappop(childRes))
                else:
                    top_two.append(0)

            print(top_two)
            res = max(res, top_two[0] + top_two[1])

            return max(top_two[0], top_two[1]) + 1

        dfs(root)
        return res