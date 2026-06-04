class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        sorted_pairs = sorted(zip(position, speed), key=lambda x: x[0], reverse = True)

        for p, s in sorted_pairs:
            t = (target - p)/s

            if len(stack) == 0:
                stack.append(t)
            else:
                if t <= stack[-1]:
                    continue
                else:
                    stack.append(t)


        return len(stack)