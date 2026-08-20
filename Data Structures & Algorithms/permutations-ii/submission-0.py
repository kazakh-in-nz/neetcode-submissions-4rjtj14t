class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            nextPerms = set()
            
            for p in perms:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i, n)
                    tupleCopy = tuple(pCopy)
                              
                    if tupleCopy not in nextPerms:
                        nextPerms.add(tupleCopy)

            perms = [[*s] for s in nextPerms]

        return perms

        