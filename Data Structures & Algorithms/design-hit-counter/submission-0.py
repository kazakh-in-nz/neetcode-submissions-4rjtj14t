class HitCounter:
    def __init__(self):
        self.store = []

    def hit(self, timestamp: int) -> None:
        self.store.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        if len(self.store) == 0:
            return 0

        t = timestamp - 300
        l, r = 0, len(self.store)

        while l < r:
            m = l + (r - l) // 2

            if self.store[m] > t:
                r = m
            else:
                l = m + 1

        left_edge = l

        l, r = 0, len(self.store)
        while l < r:
            m = l + (r - l) // 2

            if self.store[m] > timestamp:
                r = m
            else:
                l = m + 1

        right_edge = l

        return right_edge - left_edge

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
