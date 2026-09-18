class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)

            if s1 > s2:
                heapq.heappush(stones, -(s1 - s2))
            elif s2 > s1:
                heapq.heappush(stones, -(s2 - s1))
            else:
                continue

        return 0 if len(stones) == 0 else -stones[0]