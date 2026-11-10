class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []

        for key in counts:
            if counts[key] > len(nums) // 3:
                res.append(key)

        return res