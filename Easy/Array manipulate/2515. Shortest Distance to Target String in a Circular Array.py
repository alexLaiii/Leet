"""
Returns the shortest distance from startIndex to any occurrence of target
in a circular array of strings.

The array is treated as circular, so movement can be made both forward
(right) and backward (left), wrapping around the ends. The distance is
defined as the minimum number of steps required to reach an index where
words[i] == target.

The algorithm expands outward from startIndex, checking both directions
at increasing distances. The first match found guarantees the shortest
distance.

Args:
    words (List[str]): List of strings representing the circular array.
    target (str): The target string to search for.
    startIndex (int): The starting index in the array.

Returns:
    int: The minimum number of steps to reach target, or -1 if target
         does not exist in the array.

Time Complexity:
    O(n) — in the worst case, all elements are checked once.

Space Complexity:
    O(1) — constant extra space.
"""
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        N = len(words)
        currMin = N
        i = 0
        for i in range(N):
            l_idx = (startIndex - i + N) % N
            r_idx = (startIndex + i) % N
            if words[l_idx] == target or words[r_idx] == target:
                return i
        return -1
        
        
        
