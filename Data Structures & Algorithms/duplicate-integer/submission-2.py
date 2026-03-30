class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()

        for v in nums:
            if v in s:
                return True

            s.add(v)

        return False