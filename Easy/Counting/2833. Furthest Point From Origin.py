class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L_count = R_count = 0
        for m in moves:
            if m == "L":
                L_count += 1
            elif m == "R":
                R_count += 1
        
        return abs(L_count - R_count) + (len(moves) - (L_count + R_count))
        
        
