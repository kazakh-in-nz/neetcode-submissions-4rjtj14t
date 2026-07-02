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

    def isSameComponent(self, x: int, y: int) -> bool:
        x_par, y_par = self.find(x), self.find(y)
        
        return x_par == y_par

    def union(self, x: int, y: int) -> bool:
        x_par, y_par = self.find(x), self.find(y)
        
        if x_par == y_par:
            return False

        if self.rank[x_par] > self.rank[y_par]:
            self.par[y_par] = x_par
        elif self.rank[x_par] < self.rank[y_par]:
            self.par[x_par] = y_par
        else:
            self.par[y_par] = x_par
            self.rank[x_par] += 1

        self.components -= 1
        return True

    def getNumComponents(self) -> int:
        return self.components

