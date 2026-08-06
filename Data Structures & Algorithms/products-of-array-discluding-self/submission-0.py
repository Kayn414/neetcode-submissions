class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]

            res.append(product)
        return res

    
    # O(n) case computing right-left, left-right then combine
    # def productExceptSelf(nums):
    #     n = len(nums)
    #     prefix = [1] * n
    #     suffix = [1] * n
    #     result = [1] * n

    #     # prefix[i] = product of nums[0..i-1]
    #     for i in range(1, n):
    #         prefix[i] = prefix[i-1] * nums[i-1]

    #     # suffix[i] = product of nums[i+1..n-1]
    #     for i in range(n - 2, -1, -1): # n - 1 position is filled with 1
    #         suffix[i] = suffix[i+1] * nums[i+1]

    #     for i in range(n):
    #         result[i] = prefix[i] * suffix[i]

    #     return result