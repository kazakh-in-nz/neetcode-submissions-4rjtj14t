class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        self._up(len(self.heap)-1)


    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1

        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._down(1)

        return root

    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        for idx in reversed(range(1, len(self.heap) // 2 + 1)):
            self._down(idx)

    def _up(self, idx: int):
        p = idx // 2

        while idx > 1 and self.heap[p] > self.heap[idx]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]

            idx = p
            p = idx // 2

    def _down(self, idx: int):
        child = 2 * idx

        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child + 1] < self.heap[child]:
                child += 1
            
            if self.heap[child] >= self.heap[idx]:
                break

            self.heap[child], self.heap[idx] = self.heap[idx], self.heap[child]

            idx = child
            child = 2 * idx
        