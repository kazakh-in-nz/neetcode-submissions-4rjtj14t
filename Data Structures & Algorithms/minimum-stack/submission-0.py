import math

class MinStack:
    def __init__(self):
        self.s = []
        self.m = 0

    def push(self, val: int) -> None:
        if len(self.s) == 0:
            self.m = val
            self.s.append(0)
            return

        diff = val - self.m

        if diff < 0:
            self.m = val
        
        self.s.append(diff)

    def pop(self) -> None:
        t = self.s.pop()

        if t < 0:
            self.m += -1 * t

    def top(self) -> int:
        print(self.s)
        if self.s[-1] <= 0:
            return self.m
        else:
            return self.s[-1] + self.m

    def getMin(self) -> int:
        return self.m
        
