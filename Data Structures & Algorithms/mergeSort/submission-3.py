# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def _merge(self, arr: List[Pair], l: int, m: int, r: int):
        la, ra = arr[l:m+1], arr[m+1:r+1]
        il, ir, i = 0, 0, l

        while il < len(la) and ir < len(ra):
            if la[il].key <= ra[ir].key:
                arr[i] = la[il]
                il += 1
            else:
                arr[i] = ra[ir]
                ir += 1

            i += 1
        
        while il < len(la):
            arr[i] = la[il]
            il += 1
            i += 1
        
        while ir < len(ra):
            arr[i] = ra[ir]
            ir += 1
            i += 1

        
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def dfs(arr: List[Pair], l: int, r: int):
            if r - l + 1 <= 1:
                return

            m = (r + l) // 2

            dfs(arr, l, m)
            dfs(arr, m + 1, r)
            self._merge(arr, l, m, r)

        dfs(pairs, 0, len(pairs)-1)

        return pairs
