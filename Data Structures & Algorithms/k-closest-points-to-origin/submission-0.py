class Solution:
    def distance(self, x:int, y:int) -> int:
        return math.sqrt(x**2 + y**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        m = defaultdict(list)
        d = []
        for c in points:
            distance = self.distance(c[0], c[1])
            m[distance].append([c[0], c[1]])
            d.append(-1*distance)
        
        heapq.heapify(d)

        while len(d) > k:
            heapq.heappop(d)
        
        res = []
        for c in d:
            while k > 0 and m[-1*c]:
                res.append(m[-1*c].pop())
                k -= 1
        
        return res