class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {num: idx for idx, num in enumerate(nums)}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in s and i != s[diff]:
                return [i, s[diff]]
        
        return []
        