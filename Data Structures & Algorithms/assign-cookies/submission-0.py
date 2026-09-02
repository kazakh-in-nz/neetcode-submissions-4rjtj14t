class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        res = 0
        s_p = 0
        g_i = 0

        while g_i < len(g) and s_p < len(s):
            if s[s_p] < g[g_i]:
                s_p += 1
                continue

            s_p += 1
            g_i += 1
            res += 1
        
        return res