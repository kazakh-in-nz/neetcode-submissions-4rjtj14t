class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while len(stack) > 0 and stack[-1][0] < t:
                _, si = stack.pop()
                res[si] = i - si

            stack.append((t, i))

        return res