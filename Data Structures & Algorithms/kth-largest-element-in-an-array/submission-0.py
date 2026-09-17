class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * v for v in nums]
        heapq.heapify(nums)

        while k > 1:
            heapq.heappop(nums)
            k -= 1

        return -1 * heapq.heappop(nums)