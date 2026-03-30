class DynamicArray:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = []

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if len(self.arr) >= self.cap:
            self.resize()

        self.arr.append(n)

    def popback(self) -> int:
        n = self.arr.pop()
        return n

    def resize(self) -> None:
        self.cap *= 2

    def getSize(self) -> int:
        return len(self.arr)
    
    def getCapacity(self) -> int:
        return self.cap