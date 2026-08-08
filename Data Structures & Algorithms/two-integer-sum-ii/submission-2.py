class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        res = []

        while left < right:
            sum_ = numbers[left] + numbers[right]
            if sum_ == target:
                res.append(left + 1)
                res.append(right + 1)
                return res
            elif sum_ > target:
                right -= 1
            else:
                left += 1
        return res