class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in s:
                return [s[diff], i]

            s[n] = i
        
        return []
        