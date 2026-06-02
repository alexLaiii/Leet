"""
Return the earliest possible finish time after taking exactly one land ride
and one water ride, in either order.

For land -> water:
- First find the earliest possible finish time of any land ride.
- Then try each water ride as the second ride.

For water -> land:
- First find the earliest possible finish time of any water ride.
- Then try each land ride as the second ride.

Since the second ride only depends on when the first ride finishes,
choosing the earliest-finishing first ride is always optimal for each order.
"""

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        landFirst = float("inf")
        for i in range(len(landStartTime)):
            landFirst = min(landFirst, landStartTime[i] + landDuration[i])
        land_res = float("inf")
        for j in range(len(waterStartTime)):
            land_res = min(max(waterStartTime[j], landFirst) + waterDuration[j], land_res)
        
        waterFirst = float("inf")
        for i in range(len(waterStartTime)):
            waterFirst = min(waterFirst, waterStartTime[i] + waterDuration[i])
        water_res = float("inf")
        for j in range(len(landStartTime)):
            water_res = min(water_res, max(landStartTime[j], waterFirst) + landDuration[j])

        return min(land_res, water_res)
