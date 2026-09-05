class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 2) for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v,cst])
        
        dist[src][0] = 0
        minHeap = [(0,src,-1)]
        while minHeap:
            cst, node, stops = heapq.heappop(minHeap)
            if dst == node: return cst
            if stops == k or dist[node][stops + 1] < cst: 
                continue
            for neig, w, in adj[node]:
                nextCst = cst + w
                nextStops = 1 + stops
                if dist[neig][nextStops + 1] > nextCst:
                    dist[neig][nextStops + 1] = nextCst
                    heapq.heappush(minHeap, (nextCst, neig, nextStops))
        
        return -1

