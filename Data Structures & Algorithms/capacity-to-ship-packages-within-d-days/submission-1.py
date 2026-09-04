class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            new_days = 1
            temp = 0

            for w in weights:
                if temp + w > capacity:
                    new_days += 1
                    temp = w
                else:
                    temp += w

            return new_days

        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            m = l + (r - l) // 2

            new_days = check(m)

            if new_days <= days:
                res = m
                r = m - 1
            else:
                l = m + 1

        return res
