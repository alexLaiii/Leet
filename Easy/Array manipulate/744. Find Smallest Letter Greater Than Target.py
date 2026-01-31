"""
Return the smallest character in the sorted list `letters`
that is strictly greater than `target`. If no such character
exists, wrap around and return the first character.

Uses binary search to find the first letter > target in O(log n) time.
"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
    
        while l < r:
            mid = (l + r)//2
            if letters[mid] > target:
                r = mid
            else:
                l = mid + 1

        return letters[l] if letters[l] > target else letters[0]
