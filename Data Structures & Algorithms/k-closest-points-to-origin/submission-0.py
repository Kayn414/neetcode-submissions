class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dist = (x*x) + (y*y)
            heapq.heappush(heap, (dist, [x, y]))
        
        for _ in range(k):
            _, point = heapq.heappop(heap)
            res.append(point)
    
        
        return res
