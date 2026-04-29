class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        for i in range(n):
            maxL = maxR = height[i]

            for j in range(i):
                maxL = max(maxL, height[j])

            for j in range(i+1, n):
                maxR = max(maxR, height[j])

            res += min(maxL, maxR) - height[i]

        return res