"""
Idea:
Use a Max Heap structure to ensure the max is always at the top(O(1)) access
Use Lazy deletion (Check the max validation only when maximum is required, our heap don't follow the element nor the size of the window, just guranteen that the top one is the greatest, 
                    But for it to be a "valid" greatest, we need to checked its index is in the current window before adding to the result)
                    If the current top is not valid, pop until the valid one is found
                    Add to the result
return result

Example: nums = [5,4,8,3,9,5,8,4,3,2,1], k = 3
i = 0, window = [5], heap: (5,0)
i = 1, window = [5,4], heap: (5,0), (4,1)
i = 2, window = [5,4,8], heap: (8,3), (5,0), (4,1), -> maximum require, in window? idx > i - k?, 3 > 2-3, True, append (8,3) to result
i = 3, window = [4,8,3], heap: (8,3), (5,0), (4,1), (3,3) -> maximum require, in window? idx > i - k?, 3 > 3-3, True, append (8,3) to result
i = 4, window = [8,3,9], heap: (9,4), (8,3), (5,0), (4,1), (3,3) -> maximum require, in window? idx > i - k?, 4 > 4-3, True, append (9,4) to result
i = 5, window = [3,9,5], heap: (9,4), (8,3), (5,0), (5,5), (4,1), (3,3) -> maximum require, in window? idx > i - k?, 4 > 5-3, True, append (9,4) to result
i = 6, window = [9,5,8], heap: (9,4), (8,3), (8,6), (5,0), (5,5), (4,1), (3,3) -> maximum require, in window? idx > i - k?, 4 > 6-3, True, append (9,4) to result
i = 7, window = [5,8,4], heap: (9,4), (8,3), (8,6), (5,0), (5,5), (4,1), (4,7), (3,3) -> maximum require, in window? idx > i - k?, 4 > 7-3, False, pop (9,4)
                                                                                      -> (8,3) in window? idx > i - k?, 3 > 7-3, False, pop(8,3)
                                                                                      -> (8,6) in window? idx > i - k?, 6 > 7-3, True, append (8,6) to result
i = 8, window = [8,4,3], heap: (8,6), (5,0), (5,5), (4,1), (4,7), (3,3), (3,8) -> maximum require, in window? idx > i - k?, 6 > 8-3, True, append (8,6) to result
i = 9, window = [4,3,2], heap: (8,6), (5,0), (5,5), (4,1), (4,7), (3,3), (3,8), (2,9) -> maximum require, in window? idx > i - k?, 6 > 9-3, False, pop (8,6)
                                                                                       -> (5,0) in window? idx > i - k?, 0 > 9-3, False, pop(5,0)
                                                                                       -> (5,5) in window? idx > i - k?, 5 > 9-3, False, pop(5,5)
                                                                                       -> (4,1) in window? idx > i - k?, 1 > 9-3, False, pop(4,1)
                                                                                       -> (4,7) in window? idx > i - k?, 7 > 9-3, True, append (4,7) to result
i = 10, window = [3,2,1], heap: (4,7), (3,3), (3,8), (2,9) -> maximum require, in window? idx > i - k?, 7 > 10-3, False, pop (4,7)
                                                           -> (3,3) in window? idx > i - k?, 3 > 10-3, False, pop(3,3)
                                                           -> (3,8) in window? idx > i - k?, 8 > 10-3, True, append(3,8) to result

Final result: [(8,3), (8,3), (9,4), (9,4), (9,4), (8,6), (8,6), (4,7), (3,8)], excluding the index = [8,8,9,9,9,8,8,4,3]

**Note that the order of heap structure doesnt exactly looks like this, Heap only perserve first element as the min/max number and has O(1) access for popping, the interior is not guranteen sorted. **



"""


from heapq import heappush, heappop

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        maxHeap, res = [], []
        for i in range(len(nums)):
            heappush(maxHeap, (-nums[i], i))
            if i >= k - 1:
                # This indicate this max is not in the current window, we need to pop it
                while not maxHeap[0][1] > i - k:
                    heappop(maxHeap)
                res.append(-maxHeap[0][0])
        return res

