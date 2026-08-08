class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1 , n - 1 # indexes for j and k
            while left < right: # move j and k pointers
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0: # sum is correct
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: # left dups
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: # right dups
                        right -= 1
                elif sum_ < 0: # say we have [-4, -1, 0, 1, 2] -> i=4, j=-1 k=0 sum_ is -5 move j 
                    left += 1
                else: # sum_ > 0 
                    right -= 1
        return res