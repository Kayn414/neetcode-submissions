class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        res = 0

        while r < n - 1:
            furthest = 0
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])

            l = r + 1
            r = furthest
            res += 1
        return res