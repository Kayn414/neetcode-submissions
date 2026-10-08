class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for n, cnt in count.items():
            if cnt % 2 == 1:
                return False
        
        return True