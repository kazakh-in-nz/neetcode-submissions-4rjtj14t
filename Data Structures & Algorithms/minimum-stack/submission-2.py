class MinStack:
    def __init__(self):
        self.s = []
        self.sm = []

    def push(self, val: int) -> None:
        self.s.append(val)
        self.sm.append(min(val, self.sm[-1])) if len(self.sm) > 0 else self.sm.append(val) 
        

    def pop(self) -> None:
        self.s.pop()
        self.sm.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.sm[-1]
