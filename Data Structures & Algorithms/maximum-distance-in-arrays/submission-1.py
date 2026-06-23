class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res, min_v, max_v = 0, arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            res = max(res, arrays[i][-1] - min_v, max_v - arrays[i][0])
            min_v = min(min_v, arrays[i][0])
            max_v = max(max_v, arrays[i][-1])

        return res
        