class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        L, R = [1]*len(nums), [1]*len(nums)

        for i in range(len(nums)):
            prev = L[i-1] if i-1 >= 0 else 1
            L[i] *= prev * nums[i]

        for i in range(len(nums)-1, -1, -1):
            prev = R[i+1] if i+1 < len(nums) else 1
            R[i] *= prev * nums[i]

        res = []
        for i in range(len(nums)):
            l = L[i-1] if i-1 >= 0 else 1
            r = R[i+1] if i+1 < len(nums) else 1
            res.append(l*r)

        return res

        