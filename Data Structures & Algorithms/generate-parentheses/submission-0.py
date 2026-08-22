class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []
        
        def backtrack(o, c):
            if o == c == n:
                res.append("".join(curr.copy()))
                return

            if o < n:
                curr.append("(")
                backtrack(o+1, c)
                curr.pop()

            if c < o:
                curr.append(")")
                backtrack(o, c+1)
                curr.pop()

        backtrack(0, 0)
        return res

        