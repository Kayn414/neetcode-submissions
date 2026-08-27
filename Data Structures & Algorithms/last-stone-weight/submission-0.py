class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)


        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            if x == y:
                continue
            if x > y:
               y = -(y - x)
               heapq.heappush(heap, -y)
            
        return -heap[0] if heap else 0

