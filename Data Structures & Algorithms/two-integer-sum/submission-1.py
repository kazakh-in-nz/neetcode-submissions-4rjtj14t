class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_m = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in diff_m:
                return [diff_m[diff], i]

            diff_m[n] = i