from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        
        if dst not in self.adj_list:
            self.adj_list[dst] = set()

        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visited = set()
        return self._bfs(src, dst, visited)

    def _dfs(self, src: int, dst: int, visited: set) -> bool:
        if src == dst:
            return True

        visited.add(src) 

        for n in self.adj_list.get(src, []):
            if n and n not in visited:
                if self._dfs(n, dst, visited):
                    return True

        return False

    def _bfs(self, src: int, dst: int, visited: set) -> bool:
        q = deque()
        q.append(src)

        while len(q) > 0:
            for _i in range(len(q)):
                v = q.popleft()
                visited.add(v)

                if v == dst:
                    return True

                for n in self.adj_list.get(v, []):
                    if n and n not in visited:
                        q.append(n)

        return False


