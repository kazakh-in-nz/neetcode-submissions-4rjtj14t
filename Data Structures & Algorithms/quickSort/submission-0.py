# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def _qs(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs
        
        pivot = pairs[e].key
        l = s

        for i in range(s, e + 1):
            if pairs[i].key < pivot:
                pairs[l], pairs[i] = pairs[i], pairs[l]
                l += 1
        
        pairs[l], pairs[e] = pairs[e], pairs[l]
        
        self._qs(pairs, s, l - 1)
        self._qs(pairs, l + 1, e)
        return pairs

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._qs(pairs, 0, len(pairs) - 1)
        