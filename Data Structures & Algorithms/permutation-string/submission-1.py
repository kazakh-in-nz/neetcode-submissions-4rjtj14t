from collections import Counter

class Solution:
    def _compare_maps(self, m1: Dict[str, int], m2: Dict[str, int]):
        for key, val in m2.items():
            if val == 0:
                continue

            if key not in m1 or val != m1[key]:
                return False
        
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m1 = Counter(s1)
        slide_m = Counter(s2[:len(s1)])

        if self._compare_maps(m1, slide_m):
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            slide_m[s2[r]] = 1 + slide_m.get(s2[r],0)
            slide_m[s2[l]] -= 1
            l += 1

            if self._compare_maps(m1, slide_m):
                return True

        return False


        