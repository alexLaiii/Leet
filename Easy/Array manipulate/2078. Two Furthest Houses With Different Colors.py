"""
Finds the maximum distance between two houses with different colors.

This solution relies on the observation that the two furthest houses with
different colors must involve either the first house or the last house.
If a farther valid pair existed entirely in the middle, extending to one
of the ends would produce an equal or greater distance.

The algorithm scans through the array once and checks:

1. If the current house has a different color from the first house,
   update the maximum distance using its distance from index 0.

2. If the current house has a different color from the last house,
   update the maximum distance using its distance from the last index.

This guarantees the maximum valid distance in linear time.

Time Complexity:
O(n), where n is the number of houses.

Space Complexity:
O(1), since only constant extra space is used.
"""

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        N = len(colors) - 1
        maxD = -1
        for i in range(len(colors)):
            if colors[i] != colors[0]:
                maxD = max(i - 0, maxD)
            if colors[i] != colors[N]:
                maxD = max(N - i, maxD)
        return maxD
