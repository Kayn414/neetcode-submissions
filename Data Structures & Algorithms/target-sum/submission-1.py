class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # input [2,2,2] target = 2
        total = sum(nums) # 6
        if (total + target) % 2 != 0 or abs(target) > total:
            return 0
        subset = (total + target) // 2 # 8 // 2 = 4

        dp = [0] * (subset + 1) # [0,0,0,0,0] 
        dp[0] = 1 # [1,0,0,0,0]

        for num in nums:
            for j in range(subset, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset]