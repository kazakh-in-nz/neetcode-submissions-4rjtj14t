from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = Counter(s)
        
        print(c)
        for ch in t:
            if c[ch] == 0:
                return False

            c[ch] -= 1

        for v in c.values():
            if v != 0:
                return False

        return True