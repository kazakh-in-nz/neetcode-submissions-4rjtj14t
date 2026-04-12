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

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._dfs(src, dst, visited)
