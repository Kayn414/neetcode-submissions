class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for _ in range(len(bin(n)) - 2):
            res += n & 1
            n >>= 1
        return res