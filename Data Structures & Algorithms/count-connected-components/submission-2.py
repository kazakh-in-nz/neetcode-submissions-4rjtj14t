class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        u = UnionFind(n)

        for [x1, x2] in edges:
            u.union(x1, x2)

        return u.components

class UnionFind:
    def __init__(self, n: int):
        self.par = {}
        self.rank = {}
        self.components = n

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, x: int) -> int:
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        
        return x

    def union(self, x1: int, x2: int) -> bool:
        x1_par, x2_par = self.find(x1), self.find(x2)

        if x1_par == x2_par:
            return False
        
        if self.rank[x1_par] > self.rank[x2_par]:
            self.par[x2_par] = x1_par
        elif self.rank[x1_par] < self.rank[x2_par]:
            self.par[x1_par] = x2_par
        else:
            self.par[x2_par] = x1_par
            self.rank[x1_par] += 1
        
        self.components -= 1
        return True