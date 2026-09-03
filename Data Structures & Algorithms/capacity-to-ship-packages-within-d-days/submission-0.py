class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        
        def check(capacity: int) -> int:
            days_needed = 1
            current_weight = 0

            for w in weights:
                if current_weight + w > capacity:
                    days_needed += 1
                    current_weight = w
                else:
                    current_weight += w

                if days_needed > days:
                    return days_needed

            return days_needed

        res = r
        while l <= r:
            m = l + (r - l)//2

            g = check(m)

            if g <= days:
                res = m
                r = m - 1
            else:
                l = m + 1


        return res