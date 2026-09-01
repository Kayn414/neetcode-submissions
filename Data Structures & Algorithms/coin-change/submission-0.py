class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount in memo:
                return memo[amount]
            if amount == 0:
                return 0
            
            res = 1e6
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            memo[amount] = res
            return res
        minCoin = dfs(amount)
        return -1 if minCoin >= 1e6 else minCoin

