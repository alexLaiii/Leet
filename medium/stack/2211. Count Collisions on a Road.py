  """
  Count the total number of collisions between cars on a straight road.

  Each character in `directions` represents a car:
  - 'L': car moving left
  - 'R': car moving right
  - 'S': stationary car

  Collision rules:
  - 'R' -> 'S': 1 collision, resulting car becomes 'S'
  - 'R' <-> 'L': 2 collisions, both cars become 'S'
  - 'L' -> 'S': 1 collision, resulting car becomes 'S'

  This implementation scans from left to right and uses a stack to keep a
  "stable" configuration of cars that will no longer collide with each other.
  For each new car, it resolves all possible collisions with the stack's top
  (right-moving or stationary cars), updating the direction to 'S' if the car
  becomes stationary after a collision. The loop continues until no further
  collisions are possible for the current car.

  Time Complexity: O(n), since each car is pushed and popped at most once.
  Space Complexity: O(n) for the stack in the worst case.

  :param directions: String of 'L', 'R', and 'S' describing initial directions.
  :return: Total number of collisions that will occur.
  """
class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        res = 0
        for d in directions:
            while stack and d != "R" and (d != "S" or stack[-1] != "S"):
                if d == "S" and stack[-1] == "R":
                    res += 1
                elif d == "L" and stack[-1] == "R":
                    res += 2
                    d = "S"
                elif d == "L" and stack[-1] == "S":
                    res += 1
                    d = "S"

                stack.pop()
            stack.append(d)
        return res
                        

                    
                    
