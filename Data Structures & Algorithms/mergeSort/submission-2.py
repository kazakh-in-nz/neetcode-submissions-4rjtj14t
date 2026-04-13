# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def _merge(self, arr: List[Pair], s: int, m: int, e: int):
        L = arr[s:m+1]
        R = arr[m+1:e+1]

        l, r = 0, 0
        k = s

        while l < len(L) and r < len(R):
            if L[l].key <= R[r].key:
                arr[k] = L[l]
                l += 1
            elif L[l].key > R[r].key:
                arr[k] = R[r]
                r += 1

            k += 1


        while l < len(L):
            arr[k] = L[l]
            l += 1
            k += 1
        
        while r < len(R):
            arr[k] = R[r]
            r += 1
            k += 1

    def _merge_sort(self, arr: List[Pair], l: int, r:int) -> List[Pair]:
        if r - l + 1 <= 1:
            return arr

        m = (r + l) // 2

        self._merge_sort(arr, l, m)
        self._merge_sort(arr, m + 1, r)
        self._merge(arr, l, m, r)

        return arr

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self._merge_sort(pairs, 0, len(pairs)-1)

