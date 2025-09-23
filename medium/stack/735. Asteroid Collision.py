
"""
Simulate 1D asteroid collisions using a stack (LeetCode 735).

Core idea:
  - Only head-on collisions can occur when a settled asteroid is moving right (stack[-1] > 0)
    and the incoming asteroid moves left (curr < 0). All other direction pairings never meet.
  - Maintain a stack of asteroids that have “survived” so far. For each incoming asteroid,
    repeatedly resolve collisions with the stack top while the pair is head-on.

Collision rules against stack[-1]:
  - If stack[-1] > -curr : incoming asteroid explodes (don’t push it).
  - If stack[-1] < -curr : stack top explodes (pop and keep checking further left).
  - If equal magnitude     : both explode (pop and don’t push curr).

Why this works:
  - Each asteroid is pushed at most once and popped at most once. The while-loop only
    triggers for actual head-on pairs, so we examine each asteroid a constant number of times,
    giving linear time overall.

Args:
    asteroids: List of integers where sign is direction (+: right, -: left) and absolute
               value is size.

Returns:
    The final configuration of asteroids after all collisions (left to right order).

Complexity:
    Time  O(n) — each asteroid is pushed/popped at most once.
    Space O(n) — stack of surviving asteroids.

Edge notes:
    - Sequences of right-movers or left-movers never collide among themselves.
    - Long chains of pops are handled by the inner while-loop when a large left-mover
      “plows through” smaller right-movers (and vice versa if mirrored).
"""
    


# Refined version, use the fact that the only Only collision possibility is the LEFT asteroid is going right and RIGHT asteroid is going left
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # 1 as right, 0 as left
        for i in range(len(asteroids)):
            # Only collision possibility is the left one is going right and right one is going left
            # That is stack[-1] >= 0 and asteroids[i] < 0
            Add = True
            while stack and asteroids[i] < 0 <= stack[-1]:
                if stack[-1] > -asteroids[i]:
                    Add = False
                    break
                elif stack[-1] < -asteroids[i]:
                    stack.pop()
                else:
                    Add = False
                    stack.pop()
                    break
            if Add:
                stack.append(asteroids[i])
        return stack


# Here is my original self-solved version
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # 1 as right, 0 as left
        for i in range(len(asteroids)):
            r_dir = 1 if asteroids[i] >= 0 else 0
            Add = True
            while stack:
                l_dir = 1 if stack[-1] >= 0 else 0
                if l_dir - r_dir != 1:
                    break
                if abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                elif abs(asteroids[i]) < abs(stack[-1]):
                    Add = False
                    break
                else:
                    Add = False
                    stack.pop()
                    break
            if Add:
                stack.append(asteroids[i])
    
    
        return stack
