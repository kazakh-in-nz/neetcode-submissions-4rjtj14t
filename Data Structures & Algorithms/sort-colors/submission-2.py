class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def mergeSort(l, r):
            if r - l + 1 <= 1:
                return

            m = l + (r - l)//2
            mergeSort(l, m)
            mergeSort(m+1, r)

            merge(l, m, r)

        def merge(l, m, r):
            L = nums[l:m+1]
            R = nums[m+1:r+1]

            i,j,k = 0,0,l

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1


            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1

        mergeSort(0, len(nums)-1)
        return nums

