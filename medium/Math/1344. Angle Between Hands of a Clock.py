"""
Calculate the smaller angle between the hour and minute hands of a clock.

The hour hand position accounts for the minutes passed within the hour,
then the absolute difference between the two hand angles is reduced to
the smaller angle around the clock.
"""
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_deg = 360 // 12
        min_degree = 360 // 60
        abs_val = abs((((hour % 12) + minutes/60) * hour_deg) - (minutes * min_degree))
        return min(abs_val, 360 - abs_val) 
        
