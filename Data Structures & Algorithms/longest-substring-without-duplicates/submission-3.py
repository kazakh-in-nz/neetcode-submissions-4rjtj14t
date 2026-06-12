class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = []
        for ch in s:
            arr.append(ord(ch))

        res = 0
        l, st = 0, set()

        for r in range(len(arr)):
            while arr[r] in st:
                st.remove(arr[l])
                l += 1

            st.add(arr[r])


            res = max(res, len(st))
            
        return res