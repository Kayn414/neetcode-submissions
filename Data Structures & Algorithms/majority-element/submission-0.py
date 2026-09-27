class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = maxCount = 0

        for num in nums:
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res