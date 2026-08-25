class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i, remainder):
            if remainder == 0:
                res.append(curr.copy())
                return
            if remainder < 0 or i == len(nums):
                return 
            
            curr.append(nums[i])
            backtrack(i, remainder - nums[i])
            curr.pop()

            backtrack(i + 1, remainder)

        backtrack(0, target)
        return res