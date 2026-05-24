class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = [1] * len(nums)
        for i in range(1, len(nums)):
            prev[i] *= nums[i-1] * prev[i-1]

        past = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            past[i] *= nums[i+1] * past[i+1]

        res = []
        for pr, pa in zip(prev, past):
            res.append(pr*pa)

        return res
        