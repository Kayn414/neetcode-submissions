class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-t for t in freq.values()]
        heapq.heapify(heap)

        time = 0
        cd = deque()

        while heap or cd:
            time += 1

            if heap:
                cycle = heapq.heappop(heap) + 1
                if cycle < 0:
                    cd.append((time + n, cycle))
            
            if cd and cd[0][0] == time:
                heapq.heappush(heap, cd.popleft()[1])

        return time