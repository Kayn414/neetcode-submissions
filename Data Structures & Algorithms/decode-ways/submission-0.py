class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n:1}
        mapping = "0123456"

        def dfs(i):
            nonlocal mapping
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0 # 01, 02, 03, etc
            
            res = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in mapping):
                res += dfs(i + 2)
            dp[i] = res
            return res
        
        return dfs(0)
