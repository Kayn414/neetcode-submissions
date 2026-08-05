class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for num in range(len(nums)):
            for j in range(num + 1, len(nums)):
                if nums[num] + nums[j] == target:
                    res.append(num)
                    res.append(j)
                    return res
        return res
