from typing import List
from functools import reduce
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Filter out the elements equal to val
        filtered = list(filter(lambda x: x != val, nums))
        
        # Map to copy the filtered values back into the original list
        # (in-place modification requirement of the problem)
        list(map(lambda i: nums.__setitem__(i, filtered[i]), range(len(filtered))))
        
        # Reduce to compute the new length (or simply return len(filtered))
        return reduce(lambda acc, _: acc + 1, filtered, 0)