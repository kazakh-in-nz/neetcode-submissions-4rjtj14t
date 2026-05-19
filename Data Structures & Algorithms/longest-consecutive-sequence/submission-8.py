class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res, s = 0, set(nums)

        for n in nums:
            if n - 1 not in s:
                length = 1

                while n + length in s:
                    length += 1

                res = max(res, length)

        return res