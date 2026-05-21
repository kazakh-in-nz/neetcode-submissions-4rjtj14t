class Solution:
    def __init__(self):
        self.delim = "#"


    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output += "{length}{delim}{string}".format(length=len(s), delim=self.delim, string=s)
        
        return output


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            res.append(s[start:start + length])
            i = start + length

        return res
        
