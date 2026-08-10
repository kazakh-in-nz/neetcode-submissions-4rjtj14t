class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        substack = []

        def dfs(i, sum_value):
            if sum_value == target:
                res.append(substack.copy())
                return

            if i >= len(nums) or sum_value > target:
                return

            substack.append(nums[i])
            dfs(i, sum_value + nums[i])

            substack.pop()
            dfs(i+1, sum_value)

        dfs(0, 0)
        return res

        