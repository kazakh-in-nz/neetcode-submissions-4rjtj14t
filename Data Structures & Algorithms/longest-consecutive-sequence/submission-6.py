class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums.sort()
        curr, streak, res = nums[0], 0, 0
        i = 0

        while i < len(nums):
            if nums[i] != curr:
                curr = nums[i]
                streak = 0

            while i < len(nums) and nums[i] == curr:
                i += 1
            
            streak += 1
            curr += 1
            res = max(res, streak)

        return res