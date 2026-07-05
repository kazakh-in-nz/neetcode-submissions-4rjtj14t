class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            ")":"(",
            "]":"[",
            "}":"{",
        }
        
        stack = []

        for ch in s:
            if ch not in m:
                stack.append(ch)
                continue

            if len(stack) == 0 or stack[-1] != m[ch]:
                return False

            stack.pop()

        return len(stack) == 0


