"""
Beginner level
"""

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        curr = [0,0]
        for c in moves:
            match c:
                case "U":
                    curr[1] += 1
                case "D":
                    curr[1] -= 1
                case "L":
                    curr[0] -= 1
                case "R":
                    curr[0] += 1
                case _:
                    break
        return curr[0] == 0 and curr[1] == 0
        
