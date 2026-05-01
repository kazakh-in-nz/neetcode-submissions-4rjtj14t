class Solution:
    def _calc(self, operator, val1: int, val2: int):
        match operator:
            case "*":
                return val1 * val2
            case "/":
                return int(val1 / val2)
            case "+":
                return val1 + val2
            case "-":
                return val1 - val2

    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(["*", "/", "+", "-"])
        s = []

        for t in tokens:
            if t not in operators:
                s.append(int(t))
            else:
                val2 = s.pop()
                val1 = s.pop()
                s.append(self._calc(t, val1, val2))

        return s[0]
        