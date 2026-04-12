from collections import deque

class Graph:
    def __init__(self):
        self.al = {} # {src: [dst1, dst2]}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.al:
            self.al[src] = set()
        
        if dst not in self.al:
            self.al[dst] = set()

        self.al[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.al or dst not in self.al[src]:
            return False

        self.al[src].remove(dst)
        return True

    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True

        visited.add(src)

        for d in self.al[src]:
            if d not in visited:
                if self._dfs(d, dst, visited):
                    return True
        
        return False

    def _bfs(self, src: int, dst: int, visited: set) -> bool:
        q = deque()
        q.append(src)

        while len(q) > 0:
            for i in range(len(q)):
                n = q.popleft()
                if n == dst:
                    return True

                visited.add(n)

                for d in self.al[n]:
                    if d not in visited:
                        q.append(d)
        
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._dfs(src, dst, visited)
