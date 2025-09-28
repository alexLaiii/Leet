"""
RandomizedSet supports insert, remove, and getRandom in average O(1) time.

How it works:
  • Keep values in a dense list `self.nums` so valid indices are 0..len(nums)-1.
  • Track each value’s current index in `self.numToIdx` (val -> idx).
  • Insert: append val to the end of `self.nums` and record its index in `self.numToIdx`.
  • Remove: to delete `val` at index i in O(1), swap the last element into i,
    update that element’s index in `self.numToIdx`, then pop the last slot and
    delete `val` from the map. This keeps the list dense (no holes).
  • getRandom: uniformly sample an index in [0, len(nums)-1] and return the value.

Why this is O(1):
  • All operations touch only the end of the list and perform O(1) hash lookups/updates.
  • No shifting of elements is needed thanks to the swap-with-last trick.

Complexity:
  • insert / remove / getRandom: average O(1)
  • space: O(n) for the list and hash map

Notes:
  • `getRandom` assumes the set is non-empty (as per problem guarantees).
"""

class RandomizedSet:

    def __init__(self):
        self.nums =  []
        self.numToIdx = {}

    def insert(self, val: int) -> bool:
        if val in self.numToIdx:
            return False
        self.nums.append(val)
        self.numToIdx[val] = len(self.nums) - 1

        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.numToIdx:
            return False
        idx = self.numToIdx[val]
        self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
        self.numToIdx[self.nums[idx]] = idx
        self.nums.pop()
        self.numToIdx.pop(val)
        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
