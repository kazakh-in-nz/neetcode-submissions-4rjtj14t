class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        k = k % size
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1

        reverse(0, size - 1)
        reverse(0, k - 1)
        reverse(k, size - 1)
        return nums
        