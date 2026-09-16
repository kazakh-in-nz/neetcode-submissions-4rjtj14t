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
            removed = -1*heapq.heappop(d)
            m[removed].pop()

        res = []
        for v in m.values():
            while v:
                res.append(v.pop())
        
        return res