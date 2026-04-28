class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        L, R = height[l], height[r]

        while l < r:
            if L < R:
                l += 1
                L = max(L, height[l])
                res += L - height[l]
            else:
                r -= 1
                R = max(R, height[r])
                res += R - height[r]
        return res