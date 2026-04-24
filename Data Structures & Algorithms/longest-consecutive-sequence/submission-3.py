class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)

        res = 0

        for n in hs:
            if n - 1 not in hs:
                length = 1

                while (n + length) in hs:
                    length += 1
                
                res = max(length, res)

        return res