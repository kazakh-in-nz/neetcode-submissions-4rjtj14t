class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        freq = [None] * (len(nums) + 1)

        for n in nums:
            if n not in m:
                m[n] = 1
            else:
                m[n] += 1

        for key, val in m.items():
            f = freq[val]
            
            if not f:
                freq[val] = [key]
            else:
                freq[val].append(key)

        res = []

        for i in range(len(freq)-1, 0, -1):
            if freq[i] and len(freq[i]) > 0:
                for v in freq[i]:
                    res.append(v)

                    if len(res) == k:
                        return res
