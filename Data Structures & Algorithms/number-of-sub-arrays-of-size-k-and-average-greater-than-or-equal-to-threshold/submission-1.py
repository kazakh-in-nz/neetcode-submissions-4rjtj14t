class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0

        target = threshold * k
        l, sub_sum, res = 0, 0, 0

        for r in range(len(arr)):
            sub_sum += arr[r]
            
            if r - l + 1 == k:
                if sub_sum >= target:
                    res += 1
                
                sub_sum -= arr[l]
                l += 1

        return res