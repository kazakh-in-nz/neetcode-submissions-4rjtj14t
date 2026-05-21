class Solution:
    def __init__(self):
        self.delim = "#"


    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output += "{length}{delim}{string}".format(length=len(s), delim=self.delim, string=s)
        
        return output


    def decode(self, s: str) -> List[str]:
        output, i = [], 0

        while i < len(s):
            lString = ""
            while s[i] != "#":
                lString += s[i]
                i += 1
            
            l = int(lString)
            word = ""

            curr = i
            for j in range(curr+1, curr+l+1):
                word += s[j]
                i += 1

            output.append(word)
            i += 1
        
        return output

        
