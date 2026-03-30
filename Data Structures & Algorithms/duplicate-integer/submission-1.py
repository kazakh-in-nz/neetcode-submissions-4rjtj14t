class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = set()

        for n in nums:
            if n in m:
                return True

            m.add(n)
            
        return False

            
         