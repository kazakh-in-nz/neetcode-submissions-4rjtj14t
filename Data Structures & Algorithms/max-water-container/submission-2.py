class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        left, right = 0, len(heights)-1

        while left < right:
            L, R = heights[left], heights[right]

            h = min(L, R)
            v = h * (right-left)
            res = max(res, v)

            if R > L:
                left += 1
            else:
                right -= 1

        return res