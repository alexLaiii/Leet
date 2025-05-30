"""
Idea:
We need to keep track of all potentially useful elements that could become the max later —
but we discard those that are less than the current number when it arrives, because they can never be the max again.

Example: nums = [5,4,8,3,9,5,8,4,3,2,1], k = 3

Step-by-step:
i = 0, window = [4], q = [5]
i = 1, window = [5,4], q = [5, 4]
i = 2, window = [5,4,8], pop 4 and 5 → q = [8]
i = 3, window = [4,8,3], q = [8, 3]
i = 4, window = [8,3,9], pop 3 and 8 → q = [9]
i = 5, window = [3,9,5], q = [9, 5]
i = 6, window = [9,5,8], pop 5 → q = [9, 8]
i = 7, window = [5,8,4], q = [8, 4]
i = 8, window = [8,4,3], q = [8, 4, 3]
i = 9, window = [4,3,2], q = [4, 3, 2]
i = 10, window = [3,2,1], q = [3, 2, 1]

**Important Note**:
Adding smaller elements at the end is necessary because if the incoming numbers keep decreasing, 
the previous smaller numbers might become the next max. 
But if we encounter a larger number later, all smaller values before it become useless and can be popped.

Counter-example:
nums = [5, 4, 3, 2, 1], k = 3
If we only stored the max (e.g., 5), then once 5 exits the window, we’d have an empty queue — breaking the algorithm’s invariant.

**Invariant**: The first element of the queue is always the max in the current window.

Implementation Steps:
- Use a deque (double-ended queue) to store elements in decreasing order.
- For each number:
    1. Pop from the back while the number is greater than elements in the deque.
    2. Append the number (or (value, index)) to the deque.
    3. Pop from the front if it's out of the current window (index <= i - k).
    4. The front of the deque is the max → append to the result.

In code, we store (value, index) pairs to track whether a value is still inside the window.

Time Complexity: O(n)
- Each element is added and removed from the deque at most once → total operations = O(n)

Space Complexity: O(k)
- The deque stores at most k elements (the size of the window)
"""


from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # monotonic queue solution
        res, q, left = [], deque(), 0
        for right in range(len(nums)):
            while q and q[-1][0] < nums[right]:
                q.pop()
            q.append((nums[right], right))
            if q[0][1] < left:
                q.popleft()
            if right >= k - 1:
                res.append(q[0][0])
                left += 1
        return res

        
        
