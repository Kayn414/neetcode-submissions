class Solution:
    
    def findDuplicate(self, nums: List[int]) -> int:
        dup = set()

        for i in range(len(nums)):
            if nums[i] in dup:
                return nums[i]
            else:
                dup.add(nums[i])
