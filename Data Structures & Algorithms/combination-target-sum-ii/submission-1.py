class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        substack = []

        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(substack.copy())
                return

            if i >= len(candidates) or curr_sum > target:
                return

            substack.append(candidates[i])
            dfs(i+1, curr_sum + candidates[i])

            substack.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1, curr_sum)
 
        dfs(0, 0)
        return res
        