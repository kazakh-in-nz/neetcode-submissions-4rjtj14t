from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_map = defaultdict(int)

        for char in s:
            char_map[char] += 1

        for char in t:
            if not char in char_map:
                return False
            elif char_map[char] <= 0:
                return False
            else:
                char_map[char] -= 1

        for v in char_map.values():
            if v > 0:
                return False

        return True
        