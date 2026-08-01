"""
Determine whether the array contains two equal elements whose indices differ
by at most k.

Traverse the array while storing the most recent index of each value. When a
value is encountered again, compare the current index with its last recorded
index. If the distance is at most k, return True immediately. Otherwise,
update the stored index and continue scanning.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] in last_seen and abs(i - last_seen[nums[i]]) <= k:
                return True
            last_seen[nums[i]] = i
        return False
        
