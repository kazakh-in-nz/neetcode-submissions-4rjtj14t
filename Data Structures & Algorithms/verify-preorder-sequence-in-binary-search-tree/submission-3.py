class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        s = []
        min_v = -float("inf")

        for v in preorder:
            if min_v > v:
                return False

            while s and s[-1] < v:
                min_v = s.pop()

            s.append(v)

        return True
            
                

        