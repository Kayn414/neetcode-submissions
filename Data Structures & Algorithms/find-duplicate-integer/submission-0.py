class Solution:
    
    def findDuplicate(self, nums: List[int]) -> int:
        _dict = Counter(nums)

        for i, c in _dict.items():
            if c > 1:
                dup = i
        
        return dup