class Solution:
    def _getKey(self, s: string) -> string:
            vals = [0]*26
            offset = ord("a")

            for ch in s:
                idx = ord(ch) - offset

                vals[idx] += 1

            key = []

            for i, v in enumerate(vals):
                while v > 0:
                    key.append(str(i))
                    v -= 1
                
            return ",".join(c for c in key)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}

        for s in strs:
            key = self._getKey(s)

            if key not in m:
                m[key] = [s]
            else:
                m[key].append(s)


        result = []
        for v in m.values():
            result.append(v)

        return result        