class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = []
        self.helper(0, nums, [], subsets)
        return subsets

    def helper(self, i, nums, cur_set, subsets):
        if  i >= len(nums):
            subsets.append(cur_set.copy())
            return

        cur_set.append(nums[i])
        self.helper(i+1, nums, cur_set, subsets)
        cur_set.pop()

        while i < len(nums) - 1 and nums[i] == nums[i+1]:
            i += 1
            
        self.helper(i+1, nums, cur_set, subsets)
        