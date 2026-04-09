class HashTable:
    def __init__(self, capacity: int):
        self.m = {}
        self.capacity = capacity

    def insert(self, key: int, value: int) -> None:
        self.m[key] = value

        if self.getSize() / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1

        return self.m[key]

    def remove(self, key: int) -> bool:
        if key not in self.m:
            return False
        
        self.m.pop(key)
        return True

    def getSize(self) -> int:
        return len(self.m)

    def getCapacity(self) -> int:
        return self.capacity

    def resize(self) -> None:
        self.capacity *= 2 

248
123