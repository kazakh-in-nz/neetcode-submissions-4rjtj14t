class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m, a = {}, ord("a")

        for w in strs:
            arr = [0] * 26

            for ch in w:
                arr[ord(ch) - a] += 1

            key = tuple(arr)

            if key in m:
                m[key].append(w)
            else:
                m[key] = [w]
        
        res = []
        for value in m.values():
            res.append(value)

        return res


        