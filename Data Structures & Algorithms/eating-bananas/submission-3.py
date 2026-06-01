class Solution:
    def _eat(self, piles: List[int], speed: int) -> int:
        hours = 0

        for p in piles:
            hours += math.ceil(p/speed)

        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)

        while low < high:
            mid = low + (high - low) // 2

            h_temp = self._eat(piles, mid)
            print(h_temp, mid)

            if h_temp <= h:
                high = mid
            else:
                low = mid + 1

        return low
        