class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def backtrack(open_cnt, closed):
            if len(curr) == (2 * n):
                res.append("".join(curr))
                return
            
            if open_cnt < n:
                curr.append("(")
                backtrack(open_cnt + 1, closed)
                curr.pop()
            if closed < open_cnt:
                curr.append(")")
                backtrack(open_cnt, closed + 1)
                curr.pop()


        backtrack(0,0)
        return res