class Solution:
    def _calculate(self, operator: str, num1: int, num2: int) -> int:
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case "/":
                return int(num1 / num2)


    def evalRPN(self, tokens: List[str]) -> int:
        operatorSet = set(["+", "-", "*", "/"])
        stack = []
        
        for t in tokens:
            if t not in operatorSet:
                stack.append(int(t))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                stack.append(self._calculate(t, num1, num2))

        return stack[0]