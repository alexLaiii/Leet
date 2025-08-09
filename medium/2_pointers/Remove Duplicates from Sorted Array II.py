"""
Removes extra duplicates from a sorted array in-place, allowing
each unique number to appear at most twice, and returns the new length.

Approach:
---------
This uses the two-pointer technique with a duplicate counter:

- `r` (read pointer) iterates over the array from left to right.
- `l` (write pointer) tracks the position where the next valid number
  should be placed.
- `currNum` stores the current number being processed.
- `count` counts how many times `currNum` has been seen consecutively.

Logic:
1. For each element at `nums[r]`:
   - If it is the same as `currNum` and `count >= 2`, skip it 
     (because more than 2 duplicates are not allowed).
   - Otherwise, write `nums[r]` to `nums[l]` and advance `l`.
2. If the element equals `currNum`, increment `count`.
   If it's a new number, reset `currNum` to this value and set `count = 1`.
3. Continue until all elements have been processed.
4. Return `l` as the length of the modified array.

Why it works:
-------------
Because the input array is sorted, duplicates are grouped together.
By tracking how many of the current number have been added so far (`count`),
we can ensure at most two copies are kept while overwriting the array in-place.

Time Complexity:
- O(n), where n is the number of elements, since we scan the array once.

Space Complexity:
- O(1), in-place with only a few extra variables.

Example:
--------
nums = [1,1,1,2,2,3]
After processing, nums becomes [1,1,2,2,3,_] and the function returns 5.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        currNum, count = nums[0], 0
        l = 0
        for r in range(len(nums)):
            if currNum == nums[r] and count >= 2:
                continue
            nums[l] = nums[r]
            if currNum == nums[r]:
                count += 1
                l += 1
            else:
                l += 1
                currNum = nums[r]
                count = 1
        return l

