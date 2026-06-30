class Solution:
    def _skip(self, ch_lowered: str) -> bool:
        ord_a = ord("a")
        ord_z = ord("z")
        ord_0 = ord("0")
        ord_9 = ord("9")

        return not (
            ord_a <= ord(ch_lowered) <= ord_z or
            ord_0 <= ord(ch_lowered) <= ord_9
        )

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if self._skip(s[l].lower()):
                l += 1
                continue

            if self._skip(s[r].lower()):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True