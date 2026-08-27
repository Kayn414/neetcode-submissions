class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks) # A: 3, B: 1, C: 1
        heap = [-t for t in freq.values()] # max_heap 
        heapq.heapify(heap)

        time = 0
        cd = deque() # (rdy_time, remaining count of tasks)

        while heap or cd:
            time += 1 # 1 -> 2 -> 3 -> 6 -> 9

            if heap:
                task_cycle = heapq.heappop(heap) + 1 # A (-2) -> B (0) -> C (0) | A (-1) -> A (0)
                if task_cycle < 0: # put on cd A -> B -> C (A comes back)
                    cd.append((time + n, task_cycle)) # (1 + 3, -2) -> (3 + 3, -1) 
            
            if cd and cd[0][0] == time: # A is scheduled back -> A -> A
                heapq.heappush(heap, cd.popleft()[1])

        return time