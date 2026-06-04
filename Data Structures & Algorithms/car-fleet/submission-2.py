class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        
        sorted_pairs = sorted(zip(position, speed), key=lambda x: x[0])

        for i in range(len(sorted_pairs)-1, -1, -1):
            p, s = sorted_pairs[i][0], sorted_pairs[i][1]

            t = (target - p)/s

            print(p, s, t)

            if len(stack) == 0:
                stack.append(t)
            else:
                if t <= stack[-1]:
                    continue
                else:
                    stack.append(t)


        return len(stack)