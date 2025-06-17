import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # built adjenacy list
        graph = {i + 1:[] for i in range(n)}
        for u,v, w in times:
            graph[u].append((v,w))

        minHeap = [(0, k)]
        visited = set()
        t = 0
        # Dijstra shortest path algorithm
        while minHeap:
            curr = heapq.heappop(minHeap)
            if curr[1] in visited:
                continue
            visited.add(curr[1])
            # t mark the time that needed to travel to curr
            t = curr[0]
            for nn, w in graph[curr[1]]:
                heapq.heappush(minHeap, (w + curr[0], nn))
        

        return t if len(visited) == n else -1
            
            
    
        
        
