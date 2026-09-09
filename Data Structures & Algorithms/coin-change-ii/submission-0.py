class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        coins.sort()

        for i in range(n+1):
            dp[i][0] = 1  # 1 way of using zero coins

        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                if coins[i] <= a:
                    dp[i][a] = dp[i+1][a] # skip coin
                    if coins[i] <= a: # choose coin under that capacity unbound via dp[i]
                        dp[i][a] += dp[i][a - coins[i]]
        return dp[0][amount] 