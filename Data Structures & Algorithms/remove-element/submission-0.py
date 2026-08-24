class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for i, r in enumerate(nums):
            if r == val:
                continue
            
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
        
        return l
        