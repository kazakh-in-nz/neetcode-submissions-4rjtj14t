class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            m = l + (r-l)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        min_n = l

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

        if nums[min_n] == target:
            return min_n

        left = bns(0, min_n - 1) if min_n > 0 else -1
        right = bns(min_n - 1, len(nums) - 1) if min_n > 0 else bns(0, len(nums)-1)

        print(min_n)

        return left if left != -1 else right
            


        