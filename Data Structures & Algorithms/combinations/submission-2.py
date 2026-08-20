class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.helper(1, [], combs, n, k)
        return combs

    def helper(self, i, currComb, combs, n, k):
        if len(currComb) == k:
            combs.append(currComb.copy())
            return

        if i > n:
            return

        for j in range(i, n + 1):
            currComb.append(j)
            self.helper(j + 1, currComb, combs, n, k)
            currComb.pop()
        