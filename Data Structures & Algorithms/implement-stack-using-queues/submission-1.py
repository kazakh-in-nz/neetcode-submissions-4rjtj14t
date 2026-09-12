from collections import deque

class MyStack:
    def __init__(self):
        self.helper = deque([])
        self.main = deque([])

    def push(self, x: int) -> None:
        while self.main:
            self.helper.append(self.main.popleft())

        self.main.append(x)
        while self.helper:
            self.main.append(self.helper.popleft())

    def pop(self) -> int:
        return self.main.popleft()

    def top(self) -> int:
        value = self.main.popleft()
        self.push(value)
        return value
        
    def empty(self) -> bool:
        return len(self.main) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()