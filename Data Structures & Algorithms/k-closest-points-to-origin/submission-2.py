class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x, y in points:
            distance = x * x + y * y
            min_heap.append((distance, x, y))

        heapq.heapify(min_heap)

        result = []

        for _ in range(k):
            _, x, y = heapq.heappop(min_heap)
            result.append([x, y])

        return result