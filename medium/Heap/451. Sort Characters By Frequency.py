"""
Sort characters in a string by decreasing frequency.

Approach:
- Count occurrences of each character.
- Push (−freq, char) pairs into a min-heap to simulate a max-heap.
- Pop from the heap and append `char * freq` chunks to a list.
- Join chunks into the final string.

Complexity: O(n log k) time, where n = len(s), k = #distinct chars; O(n) space.
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = defaultdict(int)
        for c in s:
            char_count[c] += 1
        maxHeap = []
        for key in char_count:
            heapq.heappush(maxHeap, (-char_count[key], key))
        
        strs = []
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            strs.append(char * (-count))
        return "".join(strs)
        
