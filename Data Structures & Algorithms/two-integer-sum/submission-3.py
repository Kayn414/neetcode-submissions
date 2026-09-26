class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        sum_ = 0
        n = len(nums)
        for i in range(n):
            for j in range(1, n):
                sum_ = nums[i] + nums[j]
                if i != j and sum_ == target:
                    res.append(i)
                    res.append(j)
                    return res
        
    