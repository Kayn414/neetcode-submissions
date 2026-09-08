class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums: # XOR a ^ a = 0 else a ^ 0 = a 
            res = res ^ num
        return res
        