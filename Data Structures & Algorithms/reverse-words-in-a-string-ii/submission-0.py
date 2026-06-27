class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def _reverse(l, r):
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        l, r = 0, len(s)-1
        _reverse(l, r)

        l = 0
        for r in range(len(s)):
            if s[r] == " ":
                _reverse(l, r-1)
                l = r + 1
            elif r == len(s)-1:
                _reverse(l, r)