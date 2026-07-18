"""
Find the minimum and maximum elements in the array, then compute their
greatest common divisor using the iterative Euclidean algorithm.

The Euclidean algorithm repeatedly replaces (a, b) with (b, a % b)
until the second value becomes 0. The remaining value is the GCD.

Time Complexity:
    O(n + log(min(nums)))
        - O(n) to find the minimum and maximum values.
        - O(log(min(nums))) for the Euclidean algorithm.

Space Complexity:
    O(1)
"""

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)

        # Euclidean Algorithm
        while smallest != 0:
            remainder = largest % smallest
            largest = smallest
            smallest = remainder
        return largest
            


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        smallest = min(nums)
        largest = max(nums)
        
        return gcd(smallest, largest)
