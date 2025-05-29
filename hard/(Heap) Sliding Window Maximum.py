"""
Idea: 

"""


from heapq import heappush, heappop

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        maxHeap, res = [], []
        for i in range(len(nums)):
            heappush(maxHeap, (-nums[i], i))
            if i >= k - 1:
                # This indicate this max is not in the current window, we need to pop it
                while maxHeap[0][1] <= i - k:
                    heappop(maxHeap)
                res.append(-maxHeap[0][0])
        return res
        
