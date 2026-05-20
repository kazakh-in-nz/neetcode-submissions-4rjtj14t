class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, m = 0, defaultdict(int)

        for num in nums:
            if not m[num]:
                m[num] = m[num-1] + m[num+1] + 1
                m[num - m[num-1]] = m[num]
                m[num + m[num+1]] = m[num]

                res = max(res, m[num])

        return res