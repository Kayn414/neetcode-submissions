class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d1_dp = [1] * n
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                d1_dp[j] += d1_dp[j+1]
        return d1_dp[0]