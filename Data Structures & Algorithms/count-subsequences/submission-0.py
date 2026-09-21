class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        cache = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            # skip current character in s but also consider the character in when we check each string 
            res = dfs(i+1, j)
            if s[i] == t[j]:
                # match in either s and t or lets move just s's pointer with i
                res += dfs(i+1, j+1)
            cache[(i,j)] = res
            return res

        return dfs(0,0)
        