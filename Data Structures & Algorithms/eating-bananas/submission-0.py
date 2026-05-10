class Solution:
    def _eatBananas(self, piles: List[int], rate: int) -> int:
        h = 0

        for p in piles:
            h += math.ceil(float(p) / rate)

        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minR, maxR = 1, max(piles)
        res = maxR
        
        while minR <= maxR:
            mR = minR + (maxR - minR) // 2

            newH = self._eatBananas(piles, mR)

            if newH <= h:
                res = mR
                maxR = mR - 1
            else:
                minR = mR + 1
        
        return res

            