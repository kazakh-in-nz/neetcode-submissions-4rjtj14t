class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []

        l, r = 0, 1

        while l < len(nums):
            if nums[l] + nums[r] == target:
                return [l, r]

            if r == len(nums) - 1:
                l += 1
                r = l + 1
                continue

            r += 1

        return []
            