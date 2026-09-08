class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xorr = len(nums)
        for i in range(0, len(nums)):
            xorr ^= i ^ nums[i]
        return xorr