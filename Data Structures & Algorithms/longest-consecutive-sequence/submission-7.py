class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, s = 0, set(nums)

        for n in nums:
            curr, streak = n, 0

            while curr in s:
                curr += 1
                streak += 1

            res = max(res, streak)

        return res