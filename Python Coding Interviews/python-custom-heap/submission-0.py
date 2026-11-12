import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = [] 
    res = []
    for num in nums:
        pair = (-num, num)
        heapq.heappush(max_heap, pair)
    
    while max_heap:
        pair = heapq.heappop(max_heap)
        og_val = pair[1]
        res.append(og_val)
    return res

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
