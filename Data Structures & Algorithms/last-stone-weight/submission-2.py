class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            difference = heaviest - second

            if difference > 0:
                heapq.heappush(stones, -difference)

        return -stones[0] if stones else 0