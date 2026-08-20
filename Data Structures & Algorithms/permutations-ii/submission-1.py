class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:
            next_perms = set()
            
            for p in perms:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, n)
                    next_perms.add(tuple(p_copy))

            perms = [list(p) for p in next_perms]

        return perms

        