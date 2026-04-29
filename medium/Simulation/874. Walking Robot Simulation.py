"""
Simulation using grouped obstacles by row and column.

Idea:
- Track the robot's current position and facing direction
  (North, South, East, West).
- Use two hash maps to organize obstacles for faster lookup:
    1. Y_direction_obstacle[x] -> all obstacle y-values on the same x-coordinate
       (used when moving North or South).
    2. X_direction_obstacle[y] -> all obstacle x-values on the same y-coordinate
       (used when moving East or West).

Turning:
- Command -1 means turn right.
- Command -2 means turn left.
- Two dictionaries are used to update direction quickly.

Movement:
- For a positive command c:
    - Determine the target position if there were no obstacles.
    - Check all obstacles on the same movement line:
        * Moving North/South -> check obstacles with same x
        * Moving East/West -> check obstacles with same y
    - If an obstacle lies in the movement path,
      stop right before the closest blocking obstacle.

Distance:
- After each movement command, compute the squared Euclidean distance
  from the origin:
      x^2 + y^2
- Keep track of the maximum value reached.

Why this works:
- The robot only needs to care about obstacles directly in its path.
- Grouping obstacles by row/column avoids checking every obstacle
  in the entire grid each time.

Time Complexity:
- Building obstacle maps: O(n)
- Each movement may scan all obstacles on the same row/column
- Worst case: O(commands × obstacles)

Space Complexity:
- O(n) for storing grouped obstacles
"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # -1
        right_turn = {
            'N' : 'E',
            'E' : 'S', 
            'S' : 'W',
            'W' : 'N'
        }
        # -2
        left_turn = {
            'N' : 'W',
            'W' : 'S',
            'S' : 'E',
            'E' : 'N'
        }
        # Y movement, N,S
        Y_direction_obstacle = defaultdict(list)
        X_direction_obstacle = defaultdict(list)     
        maxDistance, currPos, currDirections = 0, [0,0], 'N'

        for x,y in obstacles:
            Y_direction_obstacle[x].append(y)
            X_direction_obstacle[y].append(x)
 
        for c in commands:
            if c == -1:
                currDirections = right_turn[currDirections]
            elif c == -2:
                currDirections = left_turn[currDirections]
            else:
           
                origin_x,origin_y = currPos
                if currDirections == 'N':
                    y = origin_y + c
                    for obs_y in Y_direction_obstacle[origin_x]:
                        if origin_y < obs_y:
                            y = min(y, obs_y - 1)
                    currPos[1] = y
                elif currDirections == "S":
                    y = origin_y - c
                    for obs_y in Y_direction_obstacle[origin_x]:
                        if origin_y > obs_y:
                            y = max(y, obs_y + 1)
                    currPos[1] = y
                elif currDirections == "E":
                    x = origin_x + c
                    for obs_x in X_direction_obstacle[origin_y]:
                        if origin_x < obs_x:
                            x = min(x, obs_x - 1)
                    currPos[0] = x
                elif currDirections == "W":
                    x = origin_x - c
                    for obs_x in X_direction_obstacle[origin_y]:
                        if origin_x > obs_x:
                            x = max(x, obs_x + 1)
                    currPos[0] = x
                
                maxDistance = max(maxDistance, (currPos[0] ** 2) + (currPos[1] ** 2))
        return maxDistance

"""
Clean solution since commands[i] is either -2, -1, or an integer in the range [1, 9]

Simulation using step-by-step movement with obstacle set lookup.

Idea:
- Store all obstacles inside a hash set for O(1) average lookup.
- Track the robot's current position (x, y) and current direction.
- Use a direction index with a fixed direction list:
    0 -> North  (0, 1)
    1 -> East   (1, 0)
    2 -> South  (0, -1)
    3 -> West   (-1, 0)

Turning:
- Command -1 means turn right:
      direction = (direction + 1) % 4
- Command -2 means turn left:
      direction = (direction - 1) % 4

Movement:
- For a positive command k:
    - Move one step at a time instead of jumping directly.
    - Before each step, check whether the next position
      is an obstacle.
    - If the next cell is blocked, stop immediately.
    - Otherwise, update the robot’s position.

Distance:
- After every successful step, compute the squared Euclidean
  distance from the origin:
      x^2 + y^2
- Keep track of the maximum value reached.

Why step-by-step works:
- Since each command moves at most 9 steps, checking one step
  at a time is efficient enough.
- Using a set makes obstacle checking fast and simple.

Time Complexity:
- Building obstacle set: O(n)
- Simulation: O(total steps), and each command is at most 9 steps
- Overall: O(commands + obstacles)

Space Complexity:
- O(n) for storing obstacles
"""
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacle_set = set(map(tuple, obstacles))

        directions = [
            (0, 1),   # North
            (1, 0),   # East
            (0, -1),  # South
            (-1, 0)   # West
        ]

        x = y = 0
        d = 0
        max_distance = 0

        for command in commands:
            if command == -1:
                d = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]

                for _ in range(command):
                    nx, ny = x + dx, y + dy

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    max_distance = max(max_distance, x * x + y * y)

        return max_distance
                    
