class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        asciiA = ord("a")

        for s in strs:
            count = [0]*26

            for ch in s:
                count[ord(ch) - asciiA] += ord(ch)

            key = tuple(count)

            if key not in m:
                m[key] = []

            m[key].append(s)

        return list(m.values())