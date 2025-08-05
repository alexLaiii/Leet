  """
  Problem:
  You are given a list of bus routes, where each route is a list of bus stops. You can board 
  a bus at any stop and ride it to any of its stops. From a given source stop, determine the 
  minimum number of buses you need to take to reach the target stop. You can switch buses at 
  common stops.

  Approach:
  - Create a map `routesBelong` that tracks which bus routes each stop belongs to.
    (i.e., stop -> list of route indices)
  - Perform Breadth-First Search (BFS) starting from the source stop.
  - Each BFS level represents taking 1 additional bus.
  - For each stop in the current queue:
      - If it is the target, return the current distance (number of buses taken).
      - Get all routes that pass through this stop.
      - For each unvisited route:
          - Add all stops on that route to the queue.
          - Mark the route as visited (so we don't reprocess the same bus).
  - If BFS completes without reaching the target, return -1 (unreachable).

  Time Complexity:
  - Let R be the number of routes, and N be the total number of stops.
  - Time: O(N + R * K), where K is the average length of each route.

  Returns:
  - Minimum number of buses to reach target, or -1 if unreachable.
  """


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        routesBelong = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                routesBelong[stop].append(i)

        dq = deque([source])
        visited = set()
        distance = 0
        while dq:
            for i in range(len(dq)):
                currStop = dq.popleft()
                if currStop == target:
                    return distance
                toRoute = routesBelong[currStop]
                for route in toRoute:
                    if route not in visited:
                        for next_stop in routes[route]:
                            dq.append(next_stop)
                        visited.add(route)
                       
            distance += 1
        return -1
