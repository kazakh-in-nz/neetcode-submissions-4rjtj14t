class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if len(self.minStack) == 0:
            self.minStack.append(val) 
        else: 
            self.minStack.append(val) if val < self.minStack[-1] else self.minStack.append(self.minStack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return -1

        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.minStack) == 0:
            return -1

        return self.minStack[-1]
        
