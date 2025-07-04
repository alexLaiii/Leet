"""
Idea:
This problem uses the same trick as 930. Binary Subarrays With Sum.

The core idea is to count the number of subarrays that have **at most k distinct elements**.
At first, this feels like an overcount — but here’s the key:

If you also count the number of subarrays with **at most (k - 1) distinct elements**,  
then the number of subarrays with **exactly k distinct elements** is just:

   atMost(k) - atMost(k - 1)

How to count the number of subarrays that have **at most k distinct elements**:
That is always == to the **size** of that subarray. Why?

  Consider 
  window = [0,1,2] with k = 3
  At this point the window has 6 subarrays that satisfy k <= 3.
  Assume the next element is 2, so we append it:
  window = [0,1,2,2]

  Now notice that the new valid subarrays generated because of the newly added [2] are:
  [0,1,2,2], [1,2,2], [2,2], [2]
  All other subarrays have already been counted before this [2] was added.
  Therefore, the increase amount is always == the size of the new valid window.

Why atMost(k) - atMost(k - 1)?  
  Because all the subarrays with at most (k - 1) distinct elements are a **subset** of those with at most k.  
  So subtracting them gives you **only** the ones that have **exactly k distinct elements**.
  
  That’s the entire trick.

For the rest, we use a sliding window with left and right pointers (l and r),  
and a hash map to track the frequency of elements inside the window.

We increment the `distinct` counter when a new element is not in the window and gets added now,  
and shrink the window from the left when we exceed the allowed number of distinct elements until it is valid again.

*** Important Notes ***

Why “I’ll just use a sliding window and count every time the window has exactly K elements” does not work in this problem:

The main problem is you don't know when to start shrinking.

  If you shrink when distinct == k:
  consider: [1,0,1,0,1] with k = 2
  At window = [1, 0], you will start shrinking, so the first [1] is no longer considered.
  But notice that [1,0,1], [1,0,1,0], [1,0,1,0,1] are all valid windows, and they all include the first [1].
  Since this algorithm discards [1] too early, those subarrays won't be counted, causing an incorrect result.

  If you shrink when distinct > k:
  consider: [1,0,1,0,3] with k = 2
  At window [1,0,1,0,3], you start shrinking.
  You will only get [0,3] as a result.
  But the result in between are all missed.
  That is [0,1,0], [0,1], [1,0] are also valid and this approach fails to count them.
  So, incorrect result again.

And therefore, this trick is the optimal solution — otherwise you have to use brute force instead, which cause O(n^2)

Time Complexity:
O(n), since def helper() is called twice and each is O(n)

Space Complexity:
O(n), worst case is every element is distinct so the map has n elements.
"""

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def helper(atMostk):
            if atMostk <= 0:
                return 0
            res, l, distinct = 0,0,0
            windows_map = {}
            for r in range(len(nums)):
                if nums[r] not in windows_map or windows_map[nums[r]] == 0:
                    distinct += 1
                windows_map[nums[r]] = 1 + windows_map.get(nums[r], 0)
                while distinct > atMostk:
                    windows_map[nums[l]] -= 1
                    if windows_map[nums[l]] == 0:
                        distinct -= 1
                    l += 1
                res += r - l + 1
            return res
            

        return helper(k) - helper(k-1)

        
