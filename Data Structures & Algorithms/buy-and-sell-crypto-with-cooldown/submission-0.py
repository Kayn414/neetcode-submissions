class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, buying):
            # input [1,3,4,0,4]
            if i >= len(prices):
                return 0
            if (i, buying) in dp: 
                return dp[(i, buying)]

            cooldown = dfs(i+1, buying)
            if buying:
                buy_profit = dfs(i+1, not buying) - prices[i]  
                dp[(i,buying)] = max(cooldown, buy_profit)  
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i,buying)] = max(cooldown, sell)
            return dp[(i,buying)]

        return dfs(0,True)
