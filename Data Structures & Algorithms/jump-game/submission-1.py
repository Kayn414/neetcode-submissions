class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[False] * n for _ in range(n)]
        dp[0][0] = True
        global_max = 0 
        step_count = 0

        for i in range(n):

            if global_max >= n - 1:
                return True
            
            if i > global_max:
                return False
            
            for jump in range(1, nums[i] + 1):
                j = i + jump
                if j >= n:
                    break
                if not dp[0][j]:
                    dp[0][j] = True
                    global_max = max(global_max, j)
                    step_count += jump

        return dp[0][-1]
                
