class Solution:
    def _find_pairs(self, nums: List[int], j: int, k: int, target: int) -> List[List[int]]:
        pairs = []
        while j < k:
            s = nums[j] + nums[k]

            if s < target:
                j += 1
            elif s > target:
                k -= 1
            else:
                pairs.append([j, k])
                j += 1
                k -= 1
        
        return pairs


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_arr = sorted(nums)
        h = set()
        res = []

        for i, n in enumerate(sorted_arr):
            if n > 0:
                break

            other_indices = self._find_pairs(sorted_arr, i+1, len(sorted_arr)-1, 0 - n)
            
            for other_idx in other_indices:
                key = (sorted_arr[i], sorted_arr[other_idx[0]], sorted_arr[other_idx[1]])

                if key not in h:
                    h.add(key)
                    res.append([sorted_arr[i], sorted_arr[other_idx[0]], sorted_arr[other_idx[1]]])

        return res