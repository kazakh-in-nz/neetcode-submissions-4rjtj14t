class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set(nums)

        res = 0

        for n in hs:
            if n - 1 not in hs:
                c = 1

                while n + 1 in hs:
                    c += 1
                    n += 1
                
                res = max(c, res)

        return res