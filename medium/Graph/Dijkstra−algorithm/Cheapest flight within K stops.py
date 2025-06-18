"""
Idea:
Using Dijkstra’s shortest path algorithm to find the shortest route that can reach the destination, and then return the price.

Logic Flow:
1. Create an adjacency list, each storing: {city1: [(dst_city1, price), (dst_city2, price)], city2: [...]}
2. Use Dijkstra’s shortest path algorithm to find the shortest route to the destination.
   (Note: "shortest" here means the cheapest total price.)
   - Since we have a k-stop limit, when k reaches 0, we cannot go any further, so we close this path by not exploring further (continue).
   - If the current city is the destination, we have reached it, and since we always search the cheapest route first, we can return the price immediately — it is guaranteed to be the smallest.
   - Add the current city and its remaining k to the visited map.
   - Go through all the cities the current city can go to by pushing them into the minHeap for later visit.
     - Remember to decrement kRemain by one before storing the next city since visiting this city uses a stop.
     - Remember to add the current price and the cost to reach the next city, since the new price represents the total cost to reach that next city.

3. If nothing gets returned during the Dijkstra search (i.e., if `city == dst` is never true), that means no path can reach the destination. Thus, return -1.

Core logic — why this pruning works:  
    if city in visited and visited[city] > kRemain: continue

Explanation:
- Because the search always starts from the cheapest route, the route with the lower price will always be checked first. If that route can reach the destination, we return immediately.
- If that cheaper route cannot reach the destination, we then search for other (more expensive) routes.
- So, if we go down a more expensive path and run into a city that was already visited earlier from a cheaper route — and that earlier visit had **more remaining stops** — then we know this current path is hopeless and should be closed.
- Why? Because this route is only being searched now since all cheaper routes have failed to reach the destination, and we are hoping this more expensive route can succeed.
  But if this path has even **less remaining stops**, that means reaching the end is impossible.
- If a previous route visited this same city with **more k left** but still couldn’t reach the destination, then with **less k left now**, we have no chance to reach it.
- So, we close this route and continue exploring other possible paths.
"""


import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:[] for i in range(n)}
        for f,t,p in flights:
            graph[f].append((t,p))

        # indicate (price, city, number of stops I can go)
        minHeap = [(0, src, k + 1)]
        visited = {}
        
        while minHeap:
            price, city, kRemain = heapq.heappop(minHeap)
            if city in visited and visited[city] > kRemain:
                continue
            if city == dst:
                return price
            if kRemain == 0:
                continue
            visited[city] = kRemain
            for c, p in graph[city]:
                heapq.heappush(minHeap, (price + p, c, kRemain - 1))

        return -1
