This problem behaves like a “sliding mountain array” — not sorted, but has directional slope patterns.

The constraints are extremely important:
1. -2³¹ <= nums[i] <= 2³¹ - 1  
2. nums[i] != nums[i + 1] for all valid i

✅ Condition 1 ensures that a peak must exist — if one side goes up, the other must go down.  
✅ Condition 2 ensures no duplicates between neighbors, so there's always a clear “greater” direction.  
This prevents edge cases like [4,5,5,5,5,5,5,4], where no strict peak would be found.

---

### 🔍 How the binary search works:

- We randomly pick a `mid` and check `nums[mid + 1]`
- If `nums[mid] < nums[mid + 1]`, then:
  → The next element might be the peak, but the **current one cannot be**
  → So move `left = mid + 1`

- If `nums[mid] > nums[mid + 1]`, then:
  → The current element **might be** the peak
  → So move `right = mid` (we don’t exclude `mid`)

We keep narrowing the range. Eventually `left == right`, which is the **peak index**.

---

### ⏱ Time and Space:
- **Time:** O(log n) — classic binary search
- **Space:** O(1) — just using pointers




class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
        
        while right > left:
            mid = (right + left) // 2

            # Ascending slope → peak must be on the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1

            # Descending slope → peak could be mid or on the left
            else:
                right = mid

        # left == right at the end → that’s the peak
        return right
