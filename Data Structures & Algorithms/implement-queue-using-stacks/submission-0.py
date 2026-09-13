class MyQueue:
    def __init__(self):
        self.main = []
        self.helper = []

    def push(self, x: int) -> None:
        while self.main:
            self.helper.append(self.main.pop())

        self.main.append(x)

        while self.helper:
            self.main.append(self.helper.pop())

    def pop(self) -> int:
        return self.main.pop()
        
    def peek(self) -> int:
        v = self.main.pop()
        self.main.append(v)
        return v
        
    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()