"""
Simulate the problem description.
Time Complexitity: O(n^2)
Space Complexitity: O(n)
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        N = len(s)
        rotate_string = s
        for i in range(N):
            if rotate_string == goal:
                return True
            rotate_string = rotate_string[1: N] + rotate_string[0]

        return False

        
