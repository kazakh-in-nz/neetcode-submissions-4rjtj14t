import math

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        v = 0

        l = 0
        r = len(heights) - 1
        while l < r:
            L, R = heights[l], heights[r]

            currV = min(L, R) * (r-l)
            v = max(currV, v)

            if R > L:
                l += 1
            else:
                r -= 1
        

        return v