  """
  Versioned key–value store (LeetCode 981).

  Spec:
    - set(key, value, ts): timestamps for the *same key* arrive in strictly increasing order.
    - get(key, t): return the value saved at the greatest timestamp <= t; if none, return "".

  Idea:
    Maintain store[key] as a sorted list of (timestamp, value) pairs. Because sets are
    appended in increasing ts, the list stays sorted. For get, binary-search for the
    rightmost index where pair.timestamp <= t and return its value.

  Invariant:
    For each key, store[key][:i] are all versions with timestamps <= the target t
    when get returns i-1 as the rightmost position.

  Complexity:
    - set: O(1) amortized append
    - get: O(log n) per key (binary search)
    - space: O(total number of set calls)

  Common pitfalls:
    - Returning the first <= t instead of the *rightmost*.
    - Forgetting empty-key / t-before-first cases.
    - Resorting lists (unnecessary) or comparing tuples incorrectly.
  """

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))
        
        

    def get(self, key: str, timestamp: int) -> str:
        container = self.map[key]
        l, r = 0, len(container) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if container[mid][0] == timestamp:
                return container[mid][1]
            if container[mid][0] > timestamp:
                r = mid - 1
            else:
                res = container[mid][1]
                l = mid + 1
        return res
                    


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
