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

        currComb.append(i)
        self.helper(i+1, currComb, combs, n, k)
        
        currComb.pop()
        self.helper(i+1, currComb, combs, n, k)
        