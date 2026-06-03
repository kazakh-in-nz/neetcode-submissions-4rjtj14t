class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r-l)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        def bns(l, r):

            while l <= r:
                m = l + (r-l)//2

                if nums[m] > target:
                    r = m - 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    return m

            return -1

        res = bns(0, pivot - 1)

        if res != -1:
            return res
        
        return bns(pivot, len(nums)-1)
            


        