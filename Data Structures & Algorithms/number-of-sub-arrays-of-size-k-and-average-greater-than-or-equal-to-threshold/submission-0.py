class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return sum(arr)

        l, sub_sum, res = 0, 0, 0

        for r in range(len(arr)):
            if r - l + 1 > k:
                sub_sum = sub_sum - arr[l] + arr[r]
                l += 1
            else:
                sub_sum += arr[r]

            if r - l + 1 == k and sub_sum / k >= threshold:
                res += 1

        return res

        