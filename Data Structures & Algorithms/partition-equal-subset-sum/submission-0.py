class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums) # input 1,2,3,4 | total is 10
        if total % 2 != 0:
            return False
        
        target = total // 2 # 5
        n = len(nums) 
        # Target + 1 bc 0 sum is always true, n + 1 for number of rows aka numbers we can sum e.g. 0, 1, [1,2] etc
        dp = [[False] * (target + 1) for _ in range(n+1)] 


        for i in range(n+1):
            dp[i][0] = True # zero sum always true
        
        for i in range(1, n + 1): # Builds dp table 
            for j in range(1, target + 1):
                if nums[i-1] <= j: # 1 <= 1 
                    # How many sums can I create with 1,  then [1,2] and so on. say we have [1,2,3]
                    # but also 6, (5) our target, and 4 
                    dp[i][j] = (dp[i-1][j] or dp[i-1][j - nums[i-1]])
                else:
                    # we can create a sum of 1, 2 , and 3 from [1,2,3]
                    dp[i][j] = dp[i-1][j]
        
        return dp[n][target]