class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set[int]()

        res = 0

        for n in nums:
            if n not in hs:
                c = 1

                lgr = n + 1
                while lgr in hs:
                    c += 1
                    lgr += 1

                sml = n - 1
                while sml in hs:
                    c += 1
                    sml -= 1

                res = max(res, c)
                hs.add(n)

        return res