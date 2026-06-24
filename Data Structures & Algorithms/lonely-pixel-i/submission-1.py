from collections import defaultdict

class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        rs, cs = defaultdict(int), defaultdict(int)

        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if picture[r][c] == "W":
                    continue

                rs[r] += 1
                cs[c] += 1

        res = 0
        for r in range(len(picture)):
            for c in range(len(picture[0])):
                if (
                    picture[r][c] == "B" and
                    rs[r] == 1 and cs[c] == 1
                ):
                    res += 1

        return res
        